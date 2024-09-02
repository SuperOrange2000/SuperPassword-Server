package com.superpassword.api.service;

import com.superpassword.api.config.Secret;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ConfigServiceImpl implements ConfigService {
    @Autowired
    private Secret secret;

    @Override
    public Secret getSecretConfig() {
        return secret;
    }
}
