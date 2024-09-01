package com.superpassword.api.exceptions;

public class AccountConflictException extends LoginException {
    public AccountConflictException() {
        super();
    }

    public AccountConflictException(String message) {
        super(message);
    }

    public AccountConflictException(String message, Throwable cause) {
        super(message, cause);
    }

    public AccountConflictException(Throwable cause) {
        super(cause);
    }
}