package com.superpassword.api.service;

import com.superpassword.api.dto.UserDTO;

public interface LoginService {
    public String signUp(UserDTO user);

    public String login(UserDTO user);
}
