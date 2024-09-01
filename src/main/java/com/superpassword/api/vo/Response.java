package com.superpassword.api.vo;

public class Response<T> {
    private T data;
    private boolean success;
    private String errorMsg;
    private int errorCode;

    public static <K> Response<K> newSuccess(K data) {
        Response<K> response = new Response<>();
        response.setSuccess(true);
        response.setData(data);
        return response;
    }

    public static <K> Response<K> newFail(int errorCode, String message) {
        Response<K> response = new Response<>();
        response.setErrorCode(errorCode);
        response.setErrorMsg(message);
        return response;
    }

    public static <K> Response<K> newFail(ErrorCode errorCode) {
        Response<K> response = new Response<>();
        response.setErrorCode(errorCode.getCode());
        response.setErrorMsg(errorCode.getMsg());
        return response;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public String getErrorMsg() {
        return errorMsg;
    }

    public void setErrorMsg(String errorMsg) {
        this.errorMsg = errorMsg;
    }

    public int getErrorCode() {
        return errorCode;
    }

    public void setErrorCode(int errorCode) {
        this.errorCode = errorCode;
    }
}
