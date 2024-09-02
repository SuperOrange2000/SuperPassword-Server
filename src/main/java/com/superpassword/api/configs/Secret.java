package com.superpassword.api.configs;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Service;

@Service
@PropertySource("classpath:secret.properties")
public class Secret {
    @Value("{jwt.key}")
    public String jwtKey;
}
