package com.superpassword.api.common.cache;

import com.alibaba.fastjson2.JSON;
import com.superpassword.api.vo.Response;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringUtils;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.Signature;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

import java.lang.reflect.Method;
import java.time.Duration;

@Aspect
@Component
public class CacheAspect {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Pointcut("@annotation(com.superpassword.api.common.cache.Cache)")
    public void pt() {
    }

    @Around("pt()")
    public Object around(ProceedingJoinPoint pjp) {
        try {
            Signature signature = pjp.getSignature();
            // 类名
            String className = pjp.getTarget().getClass().getSimpleName();
            // 调用的方法名
            String methodName = signature.getName();

            String params = getParamsHex(pjp);

            Method method = ((MethodSignature) pjp.getSignature()).getMethod();
            // 获取Cache注解
            Cache annotation = method.getAnnotation(Cache.class);
            // 缓存过期时间
            long expire = annotation.expire();
            // 缓存名称
            String name = annotation.name();
            // 先从redis获取
            String redisKey = name + "::" + className + "::" + methodName + "::" + params;
            String redisValue = redisTemplate.opsForValue().get(redisKey);
            if (StringUtils.isNotEmpty(redisValue)) {
                // log.info("走了缓存~~~,{},{}",className,methodName);
                return JSON.parseObject(redisValue, Response.class);
            }
            Object proceed = pjp.proceed();
            redisTemplate.opsForValue().set(redisKey, JSON.toJSONString(proceed), Duration.ofMillis(expire));
            // log.info("存入缓存~~~ {},{}", className, methodName);
            return proceed;
        } catch (Throwable throwable) {
            throwable.printStackTrace();
        }
        return Response.newFail(-999, "系统错误");
    }

    private String getParamsHex(ProceedingJoinPoint pjp) {
        Object[] args = pjp.getArgs();
        // 参数
        StringBuilder params = new StringBuilder();
        for (Object arg : args) {
            if (arg != null) {
                params.append(JSON.toJSONString(arg));
            }
        }
        if (StringUtils.isNotEmpty(params.toString())) {
            // 加密 以防出现key过长以及字符转义获取不到的情况
            params = new StringBuilder(DigestUtils.sha256Hex(params.toString()));
        }
        return params.toString();
    }

}
