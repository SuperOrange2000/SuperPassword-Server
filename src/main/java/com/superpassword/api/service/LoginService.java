package com.superpassword.api.service;

import com.superpassword.api.dao.User;
import com.superpassword.api.dto.UserDTO;

public interface LoginService {
    public String signUp(UserDTO user);

    public String login(UserDTO user);

    public User getUserInfoByToken(String token);
}
