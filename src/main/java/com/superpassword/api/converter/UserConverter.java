package com.superpassword.api.converter;

import com.superpassword.api.dao.User;
import com.superpassword.api.dto.UserDTO;

public class UserConverter {
    public static UserDTO convert(User user) {
        UserDTO userDTO = new UserDTO();
        userDTO.setAccount(user.getAccount());
        userDTO.setGuid(user.getGuid());
        userDTO.setNickname(user.getNickname());
        userDTO.setCreateTime(user.getCreateTime());
        userDTO.setUpdateTime(user.getUpdateTime());
        return userDTO;
    }

    public static User convert(UserDTO userDTO) {
        User user = new User();
        user.setAccount(userDTO.getAccount());
        user.setGuid(userDTO.getGuid());
        user.setNickname(userDTO.getNickname());
        user.setCreateTime(userDTO.getCreateTime());
        user.setUpdateTime(userDTO.getUpdateTime());
        return user;
    }
}
