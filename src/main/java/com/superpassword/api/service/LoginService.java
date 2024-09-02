package com.superpassword.api.service;

import com.superpassword.api.dao.User;
import com.superpassword.api.dto.UserDTO;

public interface LoginService {
    String signUp(UserDTO user);

    String login(UserDTO user);

    User getUserInfoByToken(String token);
}
