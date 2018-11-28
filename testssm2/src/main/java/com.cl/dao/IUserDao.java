package com.cl.dao;

import com.cl.model.User;

public interface IUserDao {

    User selectUser(long id);

}