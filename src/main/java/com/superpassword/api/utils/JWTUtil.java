package com.superpassword.api.utils;

import com.superpassword.api.service.ConfigService;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import org.apache.commons.codec.digest.DigestUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Date;
import java.util.UUID;

@Service
public class JWTUtil {
    @Autowired
    ConfigService configService;
    // JWT过期时间
    public static final long JWT_TTL = 60 * 60 * 1000L * 24 * 14;
    // JWT_KEY为服务器私钥，注意保密
    private final String jwtKey;

    public JWTUtil(ConfigService configService) {
        this.configService = configService;
        jwtKey = configService.getSecretConfig().jwtKey;
    }

    public String getUUID() {
        return UUID.randomUUID().toString().replaceAll("-", "");
    }

    public String createJWT(String subject) {
        JwtBuilder builder = getJwtBuilder(subject, getUUID());
        return builder.compact();
    }

    private JwtBuilder getJwtBuilder(String subject, String uuid) {
        // 自行选择加密算法
        SecretKey secretKey = generalKey();
        long nowMillis = System.currentTimeMillis();
        Date now = new Date(nowMillis);

        long expMillis = nowMillis + JWTUtil.JWT_TTL;
        Date expDate = new Date(expMillis);
        return Jwts.builder()
                .id(uuid)
                .subject(subject)
                .issuer("sg")
                .issuedAt(now)
                .signWith(secretKey)
                .expiration(expDate);
    }

    public SecretKey generalKey() {
        byte[] encodeKey = DigestUtils.sha3_256(jwtKey);
        return new SecretKeySpec(encodeKey, 0, encodeKey.length, "HmacSHA256");
    }

    public Claims parseJWT(String jwt) {
        SecretKey secretKey = generalKey();
        return Jwts.parser()
                .verifyWith(secretKey)
                .build()
                .parseSignedClaims(jwt)
                .getPayload();
    }
}
