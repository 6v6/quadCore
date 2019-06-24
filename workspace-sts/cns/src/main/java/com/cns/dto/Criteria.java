package com.cns.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@ToString
@Setter
@Getter
public class Criteria {

	private int pageNum;
	private int amount;
	private int offset;
	private String press;
	private String category;
	
	
	public Criteria() {
		this(1, 10);
		this.offset = (pageNum - 1) * amount;
	}

	public Criteria(int pageNum, int amount) {
		this.pageNum = pageNum;
		this.amount = amount;
		this.offset = (pageNum - 1) * amount;
	}

//	public Criteria(int pageNum, int amount, int offset) {
//		this.pageNum = pageNum;
//		this.amount = amount;
//		this.offset = (pageNum - 1) * amount;
//	}

}
