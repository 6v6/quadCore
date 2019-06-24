package com.example.service;
 
import java.util.List;

import javax.inject.Inject;

import org.springframework.stereotype.Service;

import com.example.dao.NewsDAO;
import com.example.dto.NewsVO; 
@Service
public class NewsServiceImpl implements NewsService {
 
    @Inject
    private NewsDAO dao;
    
    @Override
    public List<NewsVO> selectNews() throws Exception {
 
        return dao.selectNews();
    }
 
}

