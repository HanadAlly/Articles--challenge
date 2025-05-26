# Articles Code Challenge

## Overview
This project implements a system to model the relationships between Authors, Articles, and Magazines using raw SQL queries with SQLite, without SQLAlchemy. It supports one-to-many relationships (Authors to Articles, Magazines to Articles) and a many-to-many relationship (Authors to Magazines via Articles). The project includes a database schema, Python classes with SQL methods, transaction handling, and a CLI tool for interactive queries.

### Features
Database Schema: Tables for authors, magazines, and articles with foreign key constraints and indexes for performance.
Model Classes: Author, Article, and Magazine with SQL-based persistence, validation, and relationship methods.
Relationship Methods:
Author: articles(), magazines(), add_article(), topic_areas(), most_prolific().
Magazine: articles(), contributors(), article_titles(), contributing_authors(), top_publisher(), with_multiple_authors().
