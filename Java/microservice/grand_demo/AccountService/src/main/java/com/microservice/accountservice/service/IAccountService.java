package com.microservice.accountservice.service;

import com.microservice.accountservice.model.Account;

import java.util.*;

public interface IAccountService {
    List<Account> getAll();

    Optional<Account> findById(Long id);

    Optional<Account> findByUsername(String username);

    Account add(Account account);

    Account edit(Long id, Account account);

    boolean delete(Long id);

    boolean isExistById(Long id);

    boolean isExistByUsername(String name);
}
