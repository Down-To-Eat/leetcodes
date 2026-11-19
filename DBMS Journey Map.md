### DBMS Journey Map



##### Stage 0 — Prerequisites and database foundations



Start here.

Before studying DBMS, make sure you understand :



1. Basic computer science foundations
* What is data and information?
* What is a data structure?
* Basic programming concepts.
* Variables, data types, conditions, loops and functions.
* Basic understanding of files and file handling.
* Client-server architecture.
* Basic networking concepts: IP, ports, requests and responses.
2. Mathematical foundations
* Sets and set operations.
* Relations and functions.
* Basic logic and predicates.
* Cartesian products.
* Basic counting and mathematical reasoning.
3. Database fundamentals
* What is a database?
* What is a DBMS?
* Database vs DBMS.
* Database vs file system.
* Advantages and disadvantages of DBMS.
* Database applications in real-world systems.
* Relational databases vs non-relational databases.



Textbook:



Chapter 1 — Introduction



* 1.1 Database-System Applications
* 1.2 Purpose of Database Systems
* 1.3 View of Data
* 1.4 Database Languages
* 1.5 Database Design
* 1.6 Database Engine
* 1.7 Database and Application Architecture
* 1.8 Database Users and Administrators
* 1.9 History of Database Systems



#### University Unit 1



##### Stage 1 — Database architecture and ER modelling



Understand how databases are designed before learning how to query them.



1. Database architecture
- Three-schema architecture.
- External level.
- Conceptual level.
- Internal level.
- Data abstraction.
- Data independence.
  - Logical data independence.
  - Physical data independence.
- Database system architecture.
- Database users.
- Database administrator (DBA).
- Database languages.
  - DDL
  - DML
  - DCL
  - TCL
2. Data models
- What is a data model?
- Importance of data models.
- Conceptual data models.
- Logical data models.
- Physical data models.
- Relational data model.
- Hierarchical and network data models.
3. Entity-Relationship (ER) model
- Entities and entity sets.
- Attributes.
  - Simple and composite.
  - Single-valued and multivalued.
  - Derived attributes.
  - Key attributes.
- Relationships and relationship sets.
- Degree of relationships.
  - Unary.
  - Binary.
  - Ternary.
- Mapping cardinalities.
  - One-to-one.
  - One-to-many.
  - Many-to-one.
  - Many-to-many.
- Participation constraints.
  - Total participation.
  - Partial participation.
- Weak entity sets.
- Strong entity sets.
- Identifying relationships.
- ER diagrams.
- ERD design issues.
- Extended ER model (EER).
- Specialization and generalization.
- Aggregation.
4. ER-to-relational mapping
- Mapping strong entity sets.
- Mapping weak entity sets.
- Mapping one-to-one relationships.
- Mapping one-to-many relationships.
- Mapping many-to-many relationships.
- Mapping multivalued attributes.
- Mapping specialization and generalization.



Textbook:



1. \- Chapter 1 — Introduction.
2. \- Chapter 6 — Database Design Using the E-R Model.
  - 6.1 Overview of the Design Process
  - 6.2 The Entity-Relationship Model
  - 6.3 Complex Attributes
  - 6.4 Mapping Cardinalities
  - 6.5 Primary Key
  - 6.6 Removing Redundant Attributes
  - 6.7 Reducing ER Diagrams to Relational Schemas
  - 6.8 Extended E-R Features
  - 6.9 Entity-Relationship Design Issues
  - 6.10 Alternative Notations for Modeling Data
  - 6.11 Other Aspects of Database Design



##### Stage 2 — Relational database model and relational algebra



This is where you understand the mathematical foundation behind relational databases.



1. Relational database fundamentals
- Structure of relational databases.
- Relations and tables.
- Tuples and records.
- Attributes and columns.
- Domains.
- Relation schemas.
- Database schemas.
- Database instances.
- Degree and cardinality of relations.
- Relational database constraints.
- Integrity rules.
2. Keys
- Super keys.
- Candidate keys.
- Primary keys.
- Alternate keys.
- Foreign keys.
- Composite keys.
- Unique keys.
- Referential integrity.
- Entity integrity.
3. Relational algebra
Fundamental operators:
- Selection (σ).
- Projection (π).
- Union (∪).
- Set difference (−).
- Cartesian product (×).
- Rename (ρ).
Additional operators:
- Intersection.
- Joins.
  - Theta join.
  - Equi join.
  - Natural join.
  - Outer joins.
- Division.
- Grouping and aggregation.
- Ungrouping.
4. Relational calculus
- Tuple relational calculus.
- Variables and predicates.
- Existential quantification.
- Universal quantification.
- Relational calculus queries.
- Relational algebra vs relational calculus.
5. Additional relational concepts
- Relational comparison.
- Codd's rules.
- Relational schemas.
- Introduction to UML.
- Schema diagrams.



Textbook:



1. Chapter 2 — Introduction to the Relational Model.
  - 2.1 Structure of Relational Databases
  - 2.2 Database Schema
  - 2.3 Keys
  - 2.4 Schema Diagrams
  - 2.5 Relational Query Languages
  - 2.6 The Relational Algebra
2. Chapter 27 — Formal Relational Query Languages (online chapter).
For tuple relational calculus and the additional formal language concepts, use Chapter 27 alongside your university material.



#### University Unit 2



##### Stage 3 — Relational database design and normalization



This stage teaches you how to design databases without unnecessary duplication, update anomalies and inconsistent information.



1. Relational database design fundamentals
- Features of good relational database design.
- Atomic domains.
- Functional dependencies.
- Attribute closure.
- Functional dependency closure.
- Candidate key identification.
- Minimal cover.
- Lossless decomposition.
- Dependency preservation.
- Redundancy in databases.
2. Database anomalies
- Insertion anomalies.
- Update anomalies.
- Deletion anomalies.
3. Normalization
- Unnormalized relations.
- First Normal Form (1NF).
- Second Normal Form (2NF).
- Third Normal Form (3NF).
- Boyce-Codd Normal Form (BCNF).
4. Advanced normalization
- Multivalued dependencies.
- Fourth Normal Form (4NF).
- Join dependencies.
- Fifth Normal Form (5NF) — additional study.
5. Database decomposition
- Decomposition of relational schemas.
- Lossless-join decomposition.
- Dependency-preserving decomposition.
- Comparing normalized schemas.



Textbook:



1. Chapter 7 — Relational Database Design.
  - 7.1 Features of Good Relational Designs
  - 7.2 Decomposition Using Functional Dependencies
  - 7.3 Functional Dependency Theory
  - 7.4 Algorithms for Decomposition
  - 7.5 Decomposition Using Functional Dependencies
  - 7.6 Normal Forms
  - 7.7 More Normal Forms
  - 7.8 Atomic Domains and First Normal Form
  - 7.9 Database Design Process
  - 7.10 Modeling Temporal Data
2. \- Chapter 28 — Advanced Relational Database Design (online chapter).



##### Stage 4 — SQL fundamentals and database manipulation



This is one of the most important stages.

Your goal is to become comfortable writing SQL queries independently, understanding how they work and solving practical database problems.



1. SQL introduction
- Overview of SQL.
- SQL syntax.
- SQL data types.
- SQL statements.
- SQL operators.
- SQL expressions.
2. Data Definition Language (DDL)
- CREATE DATABASE.
- CREATE TABLE.
- ALTER TABLE.
- DROP TABLE.
- TRUNCATE TABLE.
- Constraints.
  - PRIMARY KEY.
  - FOREIGN KEY.
  - UNIQUE.
  - NOT NULL.
  - CHECK.
  - DEFAULT.
3. Data Manipulation Language (DML)
- INSERT.
- UPDATE.
- DELETE.
- MERGE.
4. Basic SELECT queries
- SELECT.
- DISTINCT.
- WHERE.
- Comparison operators.
- Logical operators.
- BETWEEN.
- IN.
- LIKE.
- IS NULL.
- ORDER BY.
- Limiting results.
5. SQL functions
- Single-row functions.
- String functions.
- Numeric functions.
- Date and time functions.
- Conversion functions.
- Conditional expressions.
- NULL-handling functions.
6. Aggregate functions
- COUNT().
- SUM().
- AVG().
- MIN().
- MAX().
- GROUP BY.
- HAVING.
- Aggregate filtering.
7. Joins
- INNER JOIN.
- LEFT OUTER JOIN.
- RIGHT OUTER JOIN.
- FULL OUTER JOIN.
- CROSS JOIN.
- SELF JOIN.
- Joining multiple tables.
8. Subqueries
- Single-row subqueries.
- Multiple-row subqueries.
- Nested subqueries.
- Correlated subqueries.
- EXISTS.
- NOT EXISTS.
- ANY.
- ALL.
- IN.
9. Set operations
- UNION.
- UNION ALL.
- INTERSECT.
- MINUS / EXCEPT.
10. Advanced SQL
- NULL values.
- Views.
- Updating views.
- Data dictionary views.
- Sequences.
- Synonyms.
- Index creation.
- Database security.
- SQL triggers.
- Recursive queries.
- Advanced aggregation.



Textbook:



1. Chapter 3 — Introduction to SQL.
  - 3.1 Overview of the SQL Query Language
  - 3.2 SQL Data Definition
  - 3.3 Basic Structure of SQL Queries
  - 3.4 Additional Basic Operations
  - 3.5 Set Operations
  - 3.6 Null Values
  - 3.7 Aggregate Functions
  - 3.8 Nested Subqueries
  - 3.9 Modification of the Database
2. Chapter 4 — Intermediate SQL.
3. Chapter 5 — Advanced SQL.



#### University Unit 3



SQL problem-solving practice



After learning each concept, solve problems using actual tables rather than simply memorizing syntax.



1. Use these practice patterns:
- Basic SELECT queries.
- Filtering and sorting.
- Aggregation.
- Grouping.
- Multi-table joins.
- Self joins.
- Nested queries.
- Correlated subqueries.
- Set operations.
- Ranking and analytical queries.
- Complex business queries.
2. Practice platforms:
- LeetCode Database.
- HackerRank SQL.
- SQLZoo.
- StrataScratch.



##### Stage 5 — PL/SQL and database programming



SQL allows you to retrieve and manipulate data. PL/SQL allows you to write procedural programs that interact with the database.



Important: Your textbook's contents do not show a dedicated PL/SQL chapter. Chapter 5 covers related advanced SQL concepts, but you should study Oracle PL/SQL separately using your university notes and practical material.



1. PL/SQL fundamentals
- Introduction to PL/SQL.
- SQL vs PL/SQL.
- PL/SQL block structure.
- Declaration section.
- Execution section.
- Exception-handling section.
- Variables.
- Constants.
- Data types.
- Assignment statements.
- Comments.
2. Executable statements
- SQL statements inside PL/SQL.
- SELECT INTO.
- INSERT.
- UPDATE.
- DELETE.
- Transaction statements.
3. Control structures
- IF.
- IF-ELSE.
- ELSIF.
- CASE.
- Simple LOOP.
- WHILE LOOP.
- FOR LOOP.
- EXIT and CONTINUE.
4. Composite data types
- Records.
- Collections.
- Associative arrays.
- Nested tables.
- VARRAY.
5. Cursors
- Implicit cursors.
- Explicit cursors.
- Cursor declaration.
- Cursor opening.
- Cursor fetching.
- Cursor closing.
- Cursor attributes.
- Cursor FOR loops.
- Parameterized cursors.
6. Exception handling
- Predefined exceptions.
- Non-predefined exceptions.
- User-defined exceptions.
- RAISE.
- RAISE\_APPLICATION\_ERROR.
- Exception propagation.
7. Stored procedures and functions
- Creating procedures.
- Executing procedures.
- IN, OUT and IN OUT parameters.
- Creating functions.
- Returning values.
- Calling functions from SQL statements.
- Procedures vs functions.
8. Triggers
- BEFORE triggers.
- AFTER triggers.
- Row-level triggers.
- Statement-level triggers.
- INSERT triggers.
- UPDATE triggers.
- DELETE triggers.
- Audit triggers.
- Preventing invalid database operations.
9. University practical work
- Implicit cursor programs.
- Explicit cursor programs.
- Stored procedures.
- Stored functions.
- Exception handling.
- Trigger-based audit systems.
- User-defined error messages.



#### University Unit 4



##### Stage 6 — Physical database storage and file organization



Now move from logical database design to how information is physically stored inside a computer.



1. Physical storage fundamentals
- Overview of physical storage media.
- Magnetic disks.
- Flash storage.
- SSD storage.
- Storage hierarchy.
- Volatile and non-volatile storage.
- Storage access time.
- Disk access mechanisms.
- Disk-block access.
2. RAID
- RAID fundamentals.
- RAID 0.
- RAID 1.
- RAID 5.
- RAID 6.
- RAID performance and reliability.
3. File and record organization
- Database files.
- Records and blocks.
- Fixed-length records.
- Variable-length records.
- File organization.
- Heap file organization.
- Sequential file organization.
- Hash file organization.
- Record organization.
4. Storage structures
- Row-oriented storage.
- Column-oriented storage.
- In-memory databases.
- Storage organization.
- Database storage architectures.
5. Textbook:
- Chapter 12 — Physical Storage Systems.
- Chapter 13 — Data Storage Structures.



##### Stage 7 — Indexing and hashing



Indexing is one of the most important concepts for understanding database performance.



1. Indexing fundamentals
- What is an index?
- Purpose of indexing.
- Primary indexing.
- Secondary indexing.
- Clustered and non-clustered indexing.
- Dense indexing.
- Sparse indexing.
- Multilevel indexing.
- Ordered indices.
2. Tree-based indexing
- Tree-based index structures.
- Search trees.
- B-trees.
- B+ trees.
- Insertion in B+ trees.
- Deletion in B+ trees.
- Searching in B+ trees.
- Index maintenance.
3. Hashing
- Hash functions.
- Hash tables.
- Static hashing.
- Dynamic hashing.
- Hash collisions.
- Collision resolution.
- Extendible hashing.
- Linear hashing.
4. Advanced indexing
- Bitmap indexes.
- Multikey indexes.
- Spatial indexes.
- Index selection.
- Index performance.
5. Textbook:
- Chapter 14 — Indexing.
- 14.1 Basic Concepts
- 14.2 Ordered Indices
- 14.3 B+ Tree Index Files
- 14.4 B-Tree Files
- 14.5 Multiple-Key Access
- 14.6 Bitmap Indices
- 14.7 Spatial Indices
- 14.8 Write-Optimized Index Structures
- 14.9 Bitmap Indices (additional techniques)
- 14.10 Indexing of Small and Temporal Data



##### Stage 8 — Query processing and query optimization



Understanding SQL syntax is not enough. You should understand how a DBMS actually executes a query and how to make it efficient.



1. Query processing fundamentals
- Overview of query processing.
- Query execution.
- Query evaluation.
- Query processing architecture.
- Query execution plans.
- Query evaluation algorithms.
2. Query evaluation
- Selection operation.
- Selection using indexes.
- Sorting.
- Join operation.
- Nested-loop join.
- Block nested-loop join.
- Indexed nested-loop join.
- Sort-merge join.
- Hash join.
- Duplicate elimination.
- Set operations.
3. Query cost
- Measuring query cost.
- Disk I/O cost.
- CPU cost.
- Memory usage.
- Number of disk accesses.
- Estimating query execution cost.
4. Query optimization
- Overview of query optimization.
- Query transformation.
- Heuristic optimization.
- Cost-based optimization.
- Query equivalence.
- Selection pushdown.
- Projection pushdown.
- Join ordering.
- Join optimization.
- Cardinality estimation.
- Selectivity estimation.
- Query plan selection.
5. Advanced optimization
- Materialized views.
- Query optimization using indexes.
- Statistics and histograms.
- Optimizing complex queries.
- Analyzing execution plans.
6. Textbook:
- Chapter 15 — Query Processing.
- Chapter 16 — Query Optimization.



##### Stage 9 — Transaction management



Transactions are essential for understanding how databases maintain correctness when multiple operations happen together.



1. Transaction fundamentals
- What is a transaction?
- Transaction states.
- Transaction operations.
- Transaction boundaries.
- COMMIT.
- ROLLBACK.
- SAVEPOINT.
2. ACID properties
- Atomicity.
- Consistency.
- Isolation.
- Durability.
3. Transaction scheduling
- Serial schedules.
- Concurrent schedules.
- Serializability.
- Conflict serializability.
- View serializability.
- Precedence graphs.
- Testing for serializability.
4. Isolation levels
- Read uncommitted.
- Read committed.
- Repeatable read.
- Serializable.
- Dirty reads.
- Non-repeatable reads.
- Phantom reads.
5. Textbook:
- Chapter 17 — Transactions.



#### University Unit 5



##### Stage 10 — Concurrency control



Learn how database systems handle multiple users accessing and modifying data simultaneously.



1. Concurrency fundamentals
- Why concurrency control is necessary.
- Concurrent transaction execution.
- Lost updates.
- Dirty reads.
- Incorrect summaries.
- Inconsistent retrievals.
2. Lock-based protocols
- Shared locks.
- Exclusive locks.
- Lock compatibility.
- Two-phase locking (2PL).
- Strict two-phase locking.
- Rigorous two-phase locking.
- Lock conversion.
3. Deadlock management
- Deadlock conditions.
- Deadlock prevention.
- Deadlock avoidance.
- Deadlock detection.
- Deadlock recovery.
- Wait-for graphs.
4. Multiple-granularity locking
- Database-level locks.
- Table-level locks.
- Page-level locks.
- Row-level locks.
- Intention locks.
- Multiple-granularity protocols.
5. Timestamp-based protocols
- Timestamp ordering.
- Read timestamps.
- Write timestamps.
- Basic timestamp protocol.
- Thomas write rule.
6. Advanced concurrency
- Optimistic concurrency control.
- Multiversion concurrency control (MVCC).
- Snapshot isolation.
- Validation-based protocols.
7. Textbook:
- Chapter 18 — Concurrency Control.



##### Stage 11 — Database recovery systems



Understand how a DBMS recovers from crashes, failures and incomplete transactions.



1. Recovery fundamentals
- Importance of database recovery.
- Failure classification.
- Transaction failures.
- System crashes.
- Disk failures.
- Database consistency after failure.
2. Recovery and atomicity
- Log-based recovery.
- Write-ahead logging.
- Deferred database modification.
- Immediate database modification.
- Checkpoints.
- Undo operations.
- Redo operations.
- Undo/Redo recovery.
3. Recovery algorithms
- Log-based recovery algorithms.
- Checkpoint-based recovery.
- Shadow paging.
- Crash recovery.
- Recovery management.
4. Backup and recovery
- Database backup.
- Full backup.
- Incremental backup.
- Differential backup.
- Database restoration.
- Point-in-time recovery.
5. Distributed recovery concepts
- Two-phase commit (2PC).
- Coordinator and participants.
- Prepare phase.
- Commit phase.
- Failure handling.
For distributed transaction processing, additionally consult Chapter 23.
6. Textbook:
- Chapter 19 — Recovery System.
- Chapter 23 — Parallel and Distributed Transaction Processing (selected topics).



#### University Unit 5



Advanced DBMS — Beyond University Syllabus



After completing Stages 0–11, you will have covered the major foundations and topics of your university DBMS syllabus.



The following stages will help you understand modern database systems and prepare for more serious software projects.



##### Stage 12 — Advanced database architectures



1. Centralized database systems.
2. Client-server database systems.
3. Database server architectures.
4. Distributed database systems.
5. Parallel database systems.
6. Shared-memory architecture.
7. Shared-disk architecture.
8. Shared-nothing architecture.
9. Distributed storage.
10. Database scalability.
11. High availability.
12. Textbook:
- Chapter 20 — Database-System Architectures.
- Chapter 21 — Parallel and Distributed Storage.
- Chapter 22 — Parallel and Distributed Query Processing.



##### Stage 13 — Distributed databases



1. Distributed database fundamentals.
2. Data fragmentation.
3. Horizontal fragmentation.
4. Vertical fragmentation.
5. Data replication.
6. Data distribution.
7. Distributed query processing.
8. Distributed transactions.
9. Distributed concurrency control.
10. Distributed recovery.
11. Distributed consistency.
12. Textbook:
- Chapter 21 — Parallel and Distributed Storage.
- Chapter 22 — Parallel and Distributed Query Processing.
- Chapter 23 — Parallel and Distributed Transaction Processing.



##### Stage 14 — Advanced database technologies



1. Advanced indexing
- Advanced indexing techniques.
- Spatial indexing.
- Multidimensional indexing.
- Index structures for large datasets.
2. Textbook: Chapter 24 — Advanced Indexing Techniques.
3. Advanced application development
- Database application architecture.
- Database connectivity.
- Application development.
- Database-backed applications.
4. Textbook: Chapter 25 — Advanced Application Development.
5. Big data and analytics
- Big data fundamentals.
- Distributed data processing.
- Data warehousing concepts.
- Data mining.
- Data analytics.
- Graph databases.
- Data science applications.
6. Textbook:
- Chapter 10 — Big Data.
- Chapter 11 — Data Analytics.
7. Modern database models
- Object-oriented databases.
- XML databases.
- Information retrieval.
- PostgreSQL.
- Blockchain databases.
8. Textbook:
- Chapter 8 — Complex Data Types.
- Chapter 26 — Blockchain Databases.
- Chapters 29–32 — Online Chapters.

