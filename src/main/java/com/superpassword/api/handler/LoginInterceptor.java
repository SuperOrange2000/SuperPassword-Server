package com.superpassword.api.handler;

import com.alibaba.fastjson2.JSON;
import com.superpassword.api.dao.User;
import com.superpassword.api.service.LoginService;
import com.superpassword.api.vo.ErrorCode;
import com.superpassword.api.vo.Response;
import io.micrometer.common.util.StringUtils;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;

import io.jsonwebtoken.security.SignatureException;
import reactor.util.annotation.NonNull;

@Component
public class LoginInterceptor implements HandlerInterceptor {
    @Autowired
    LoginService loginService;

    @Override
    public boolean preHandle(@NonNull HttpServletRequest request, @NonNull HttpServletResponse response, @NonNull Object handler) throws Exception {
        if (!(handler instanceof HandlerMethod))
            return true;
        String token = request.getHeader("Authorization");
        if (StringUtils.isBlank(token)) {
            responseFail(response);
            return false;
        }
        try {
            User user = loginService.getUserInfoByToken(token);
            if (user == null) {
                responseFail(response);
                return false;
            }
        } catch (SignatureException e) {
            responseFail(response);
            return false;
        }
        return true;
    }

    private void responseFail(@NonNull HttpServletResponse response) throws java.io.IOException {
        Response<Void> result = Response.newFail(ErrorCode.NO_LOGIN);
        response.setStatus(403);
        response.setContentType("application/json;charset=utf-8");
        response.getWriter().print(JSON.toJSONString(result));
    }
}
