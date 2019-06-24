package com.cns.dto;

import java.sql.Date;

import lombok.Data;

@Data
public class UserVO {
 
	
    private int user_id;
    private String email;
    private String password;
    private String gender;
    private Date date_of_birth;
   

 
}

