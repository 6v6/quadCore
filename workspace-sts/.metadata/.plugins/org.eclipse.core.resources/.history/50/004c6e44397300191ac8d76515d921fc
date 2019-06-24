package com.cns.service;
 
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cns.dao.NewsDAO;
import com.cns.dto.NewsVO;

import lombok.Setter; 
@Service
public class NewsServiceImpl implements NewsService {
 
    @Setter(onMethod_ = @Autowired)
    private NewsDAO dao;
    
    @Override
    public List<NewsVO> selectNews() throws Exception {
 
        return dao.selectNews();
    }
 
}

