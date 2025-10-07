-- Databricks notebook source
REVOKE USE CATALOG ON CATALOG prod_ecommerce FROM `team-developers`;
REVOKE USE SCHEMA ON SCHEMA prod_ecommerce.bronze FROM `team-developers`;
REVOKE USE SCHEMA ON SCHEMA prod_ecommerce.golden FROM `team-analitics`;
