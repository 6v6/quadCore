package com.cns.dto;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Setter
@Getter
public class ScrapVO {

	private Long news_id;
	private int user_id;
	
	public ScrapVO( int user_id, Long news_id) {
		this.news_id = news_id;
		this.user_id = user_id;
	}

	

}
