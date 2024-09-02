package com.superpassword.api.exception;

public class ArgumentNullException extends LoginException {
    public ArgumentNullException() {
        super();
    }

    public ArgumentNullException(String message) {
        super(message);
    }

    public ArgumentNullException(String message, Throwable cause) {
        super(message, cause);
    }

    public ArgumentNullException(Throwable cause) {
        super(cause);
    }
}