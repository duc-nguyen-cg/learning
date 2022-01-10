package com.microservice.accountservice.controller;

import com.microservice.accountservice.model.Account;
import com.microservice.accountservice.service.IAccountService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/accounts")
public class AccountController {
    @Autowired
    private IAccountService accountService;

    @GetMapping
    public ResponseEntity<Iterable<Account>> getAllAccounts(){
        Iterable<Account> accounts = accountService.getAll();
        if (accounts.iterator().hasNext()){
            return new ResponseEntity<>(accounts, HttpStatus.OK);
        }
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Account> findAccountById(@PathVariable("id") Long id){
        Optional<Account> accountOptional = accountService.findById(id);
        if (accountOptional.isPresent()){
            return new ResponseEntity<>(accountOptional.get(), HttpStatus.OK);
        }
        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @PostMapping
    public ResponseEntity<Account> addAccount(@RequestBody Account account){
        return null;
    }

    @PutMapping("/{id}")
    public ResponseEntity<Account> editAccount(@PathVariable("id") Long id, @RequestBody Account account){
        return null;
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Account> deleteAccount(@PathVariable("id") Long id){
        return null;
    }
}
