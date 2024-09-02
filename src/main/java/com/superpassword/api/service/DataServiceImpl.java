package com.superpassword.api.service;

import com.alibaba.fastjson2.JSON;
import com.superpassword.api.converter.InfoGroupConverter;
import com.superpassword.api.dao.InfoGroup;
import com.superpassword.api.dao.InfoGroupRepository;
import com.superpassword.api.dao.User;
import com.superpassword.api.dto.InfoGroupDTO;
import com.superpassword.api.exception.DataNotFoundException;
import io.jsonwebtoken.security.SignatureException;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

@Service
public class DataServiceImpl implements DataService {
    @Autowired
    private InfoGroupRepository infoGroupRepository;

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Autowired
    private LoginService loginService;

    @Override
    public InfoGroupDTO getByGuid(String token, String guid) throws SignatureException {
        User owner = loginService.getUserInfoByToken(token);
        String redisJsonString = redisTemplate.opsForValue().get("DATA_" + owner.getId() + '_' + guid);
        InfoGroup infoGroup;
        if (StringUtils.isBlank(redisJsonString)) {
            infoGroup = infoGroupRepository.findByOwnerIdAndGuid(owner.getId(), guid).orElseThrow(DataNotFoundException::new);
            redisTemplate.opsForValue().set("DATA_" + owner.getId() + '_' + guid, JSON.toJSONString(infoGroup), 1, TimeUnit.HOURS);
        } else {
            infoGroup = JSON.parseObject(redisJsonString, InfoGroup.class);
        }
        return InfoGroupConverter.convert(infoGroup);
    }

    @Override
    public long addNewInfoGroup(String token, InfoGroupDTO infoGroupDTO) throws SignatureException {
        User owner = loginService.getUserInfoByToken(token);
        infoGroupDTO.setCreateTime(LocalDateTime.now());
        infoGroupDTO.setUpdateTime(LocalDateTime.now());
        InfoGroup infoGroup = InfoGroupConverter.convert(infoGroupDTO);
        infoGroup.setOwnerId(owner.getId());
        infoGroupRepository.save(infoGroup);
        redisTemplate.opsForValue().set("DATA_" + owner.getId() + '_' + infoGroup.getGuid(), JSON.toJSONString(infoGroup), 1, TimeUnit.HOURS);
        return infoGroup.getId();
    }

    @Override
    @Transactional
    public long updateInfoGroup(String token, String guid, byte[] site, byte[] username, byte[] password) {
        User owner = loginService.getUserInfoByToken(token);
        InfoGroup infoGroup = infoGroupRepository.findByOwnerIdAndGuid(owner.getId(), guid).orElseThrow(DataNotFoundException::new);
        boolean modifyFlag = false;
        if (site != null && !Arrays.equals(site, infoGroup.getSite())) {
            infoGroup.setSite(site);
            modifyFlag = true;
        }
        if (username != null && !Arrays.equals(username, infoGroup.getUsername())) {
            infoGroup.setUsername(username);
            modifyFlag = true;
        }
        if (password != null && !Arrays.equals(password, infoGroup.getPassword())) {
            infoGroup.setPassword(password);
            modifyFlag = true;
        }
        if (modifyFlag) {
            infoGroup.setUpdateTime(LocalDateTime.now());
            infoGroupRepository.save(infoGroup);
            redisTemplate.opsForValue().set("DATA_" + owner.getId() + '_' + infoGroup.getGuid(), JSON.toJSONString(infoGroup), 1, TimeUnit.HOURS);
        }
        return infoGroup.getId();
    }

    @Override
    public long deleteInfoGroup(String token, String guid) {
        User owner = loginService.getUserInfoByToken(token);
        InfoGroup infoGroup = infoGroupRepository.findByOwnerIdAndGuid(owner.getId(), guid).orElseThrow(DataNotFoundException::new);
        infoGroupRepository.delete(infoGroup);
        redisTemplate.delete("DATA_" + owner.getId() + '_' + guid);
        return infoGroup.getId();
    }
}
