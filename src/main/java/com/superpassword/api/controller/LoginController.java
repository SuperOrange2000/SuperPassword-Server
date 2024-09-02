package com.superpassword.api.controller;

import com.superpassword.api.exception.AccountConflictException;
import com.superpassword.api.exception.AccountOrPasswordException;
import com.superpassword.api.exception.ArgumentNullException;
import com.superpassword.api.vo.ErrorCode;
import com.superpassword.api.vo.Response;
import com.superpassword.api.dto.UserDTO;
import com.superpassword.api.service.LoginService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoginController {
    @Autowired
    LoginService loginService;

    @PostMapping("/sign-up")
    public Response<String> signUp(@RequestBody UserDTO userDTO) {
        try {
            String token = loginService.signUp(userDTO);
            return Response.newSuccess(token);
        } catch (AccountConflictException e) {
            return Response.newFail(ErrorCode.ACCOUNT_CONFLICT);
        } catch (ArgumentNullException e) {
            return Response.newFail(ErrorCode.PARAMS_ERROR);
        }
    }

    @PostMapping("/login")
    public Response<String> login(@RequestBody UserDTO userDTO) {
        try {
            String token = loginService.login(userDTO);
            return Response.newSuccess(token);
        } catch (AccountOrPasswordException e) {
            return Response.newFail(ErrorCode.ACCOUNT_PWD_NOT_EXIST);
        } catch (ArgumentNullException e) {
            return Response.newFail(ErrorCode.PARAMS_ERROR);
        }
    }
}
