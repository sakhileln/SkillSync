"""Sample response data from Google Firebase."""

incorrect = {
    "error": {
        "code": 400,
        "message": "INVALID_LOGIN_CREDENTIALS",
        "errors": [
            {
                "message": "INVALID_LOGIN_CREDENTIALS",
                "domain": "global",
                "reason": "invalid",
            }
        ],
    }
}

correct = {
    "kind": "identitytoolkit#VerifyPasswordResponse",
    "localId": "MMASbsdjhAKSJnad7NBD",
    "email": "sakhile@spacex.com",
    "displayName": "",
    # pylint: disable=line-too-long
    "idToken": "eyJhbGciKAJBDSMDNbsdkjdfhjALDJBHJSdksfJKV1QifQ.esdjhfdfbbvdbpwnBsTwxJXQ-CGPEdSup-XbMqlmcJTLVAJ7_jshfRWCJD6Q",
    "expiresIn": "3600",
}


users = [
    None,
    {
        "email": "sakhi@example.com",
        "expertise": "Python",
        "name": "Sakhile",
        "role": "mentee",
    },
    {
        "email": "kyle@dsquad.co.za",
        "expertise": "Python",
        "name": "Kyle",
        "role": "mentor",
    },
]
