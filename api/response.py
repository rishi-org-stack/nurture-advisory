errors= {
    400:{
        "status_code":"400_BAD_REQUEST",
        "error_text":"BAD_REQUEST",
        # "soln":"either name or hpto_url is mising"
    },
    401:{
        "status_code":"401_AUTHENTICATION_ERROR" ,
        
    },403:{
        "status_code":403,
        "error_text":"size is not entered",
        "soln":"put some values in size box"
    },
    404:{
        "status_code":404,
        "error_text":"no pizza of this size is present to update",
        "soln":"/size/"
    }
}

success ={
    200:{
        "status_code":"200" + "_ok",
        "success":"done",

    },
    201:{
        "status_code":201,
        "success":"pizza is successfully added",

    },
    202:{
        "status_code":202,
        "success":"pizza is successfully updated",
    },
    203:{
        "status_code":202,
        "success":"pizza is successfully deleted",
    }
}
