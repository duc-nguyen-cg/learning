package com.microservice.accountservice.service;

import com.microservice.accountservice.model.Account;
import com.microservice.accountservice.repository.IAccountRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class AccountService implements IAccountService{
    @Autowired
    private IAccountRepository accountRepository;

    @Override
    public List<Account> getAll() {
        return accountRepository.findAll();
    }

    @Override
    public Optional<Account> findById(Long id) {
        return accountRepository.findById(id);
    }

    @Override
    public Optional<Account> findByUsername(String username) {
        return accountRepository.findByUsername(username);
    }

    @Override
    public Account add(Account account) {
        if (account.getUsername() != null && accountRepository.existsByUsername(account.getUsername())){
            return null;
        }
        return accountRepository.save(account);
    }

    @Override
    public Account edit(Long id, Account account) {
        if (accountRepository.existsById(id)){
            if (account.getUsername() != null && accountRepository.existsByUsername(account.getUsername())) {
                account.setId(id);
                return accountRepository.save(account);
            }
        }
        return null;
    }

    @Override
    public boolean delete(Long id) {
        if (accountRepository.existsById(id)){
            accountRepository.deleteById(id);
            return true;
        }
        return false;
    }

    @Override
    public boolean isExistById(Long id) {
        return accountRepository.existsById(id);
    }

    @Override
    public boolean isExistByUsername(String name) {
        return accountRepository.existsByUsername(name);
    }


}
