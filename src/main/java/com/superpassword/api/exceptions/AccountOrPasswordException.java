package com.superpassword.api.exceptions;

public class AccountOrPasswordException extends LoginException {
    public AccountOrPasswordException() {
        super();
    }

    public AccountOrPasswordException(String message) {
        super(message);
    }

    public AccountOrPasswordException(String message, Throwable cause) {
        super(message, cause);
    }

    public AccountOrPasswordException(Throwable cause) {
        super(cause);
    }
}
