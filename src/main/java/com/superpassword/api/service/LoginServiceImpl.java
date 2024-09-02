package com.superpassword.api.service;

import com.alibaba.fastjson.JSON;
import com.superpassword.api.converter.UserConverter;
import com.superpassword.api.dao.User;
import com.superpassword.api.dao.UserRepository;
import com.superpassword.api.dto.UserDTO;
import com.superpassword.api.exception.AccountConflictException;
import com.superpassword.api.exception.AccountOrPasswordException;
import com.superpassword.api.exception.ArgumentNullException;
import com.superpassword.api.utils.JWTUtil;
import io.jsonwebtoken.Claims;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.RandomStringUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.Base64;
import java.util.concurrent.TimeUnit;

@Service
public class LoginServiceImpl implements LoginService {
    @Autowired
    private UserRepository userRepository;

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Autowired
    private JWTUtil jwtUtil;

    @Override
    @Transactional
    public String signUp(UserDTO userDTO) throws ArgumentNullException {
        String account = userDTO.getAccount();
        String password = userDTO.getPassword();
        if (StringUtils.isBlank(account) || StringUtils.isBlank(password)) {
            throw new ArgumentNullException();
        }
        User user = userRepository.findByAccount(account).orElse(null);
        if (user != null)
            throw new AccountConflictException();

        user = UserConverter.convert(userDTO);
        user.setSalt(RandomStringUtils.randomAlphanumeric(32));

        byte[] bpwd = DigestUtils.sha3_256(password + user.getSalt());
        String pwd = Base64.getEncoder().encodeToString(bpwd);
        user.setPassword(pwd);

        user.setCreateTime(LocalDateTime.now());
        user.setUpdateTime(LocalDateTime.now());
        userRepository.save(user);

        // 登录成功，使用JWT生成token，返回token和redis中
        String token = jwtUtil.createJWT(user.getGuid());
        // redisTemplate.opsForValue().set("TOKEN_" + token, JSON.toJSONString(user), 1, TimeUnit.DAYS);
        return token;
    }

    @Override
    public String login(UserDTO userDTO) throws ArgumentNullException, AccountOrPasswordException {
        String account = userDTO.getAccount();
        String password = userDTO.getPassword();
        if (StringUtils.isBlank(account) || StringUtils.isBlank(password)) {
            throw new ArgumentNullException();
        }
        User user = userRepository.findByAccount(account).orElseThrow(AccountOrPasswordException::new);

        byte[] bpwd = DigestUtils.sha3_256(password + user.getSalt());
        String pwd = Base64.getEncoder().encodeToString(bpwd);

        if (!user.getPassword().equals(pwd)) {
            throw new AccountOrPasswordException();
        }
        // 登录成功，使用JWT生成token，返回token和redis中
        String token = jwtUtil.createJWT(user.getGuid());
        redisTemplate.opsForValue().set("TOKEN_" + token, JSON.toJSONString(user), 1, TimeUnit.DAYS);
        return token;
    }

    @Override
    public User getUserInfoByToken(String token) {
        Claims claims = jwtUtil.parseJWT(token);
        String guid = claims.getSubject();
        String userJson = redisTemplate.opsForValue().get("TOKEN_" + token);
        User user;
        if (StringUtils.isBlank(userJson)) {
            user = userRepository.findByGuid(guid).orElseThrow(RuntimeException::new);
            redisTemplate.opsForValue().set("TOKEN_" + token, JSON.toJSONString(user), 1, TimeUnit.DAYS);
        } else {
            user = JSON.parseObject(userJson, User.class);
        }
        return user;
    }
}
