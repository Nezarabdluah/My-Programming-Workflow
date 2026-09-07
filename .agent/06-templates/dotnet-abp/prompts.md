# .NET ABP Prompts — .NET-Specific Prompts

> Ready-to-use prompts dedicated to .NET 8 + ABP + Angular + SQL Server

---

## 1. Creating a full DDD entity
```
Create entity [Name] with properties: [list]

Required:
- Entity inheriting from FullAuditedAggregateRoot<Guid>
- All properties with private set
- A static Create factory + an Update method
- Check.NotNullOrWhiteSpace for validation
- Repository Interface in the Domain
- AppService using domain methods (no ObjectMapper in Update)
- Fluent API configuration
- Migration
```

## 2. Fixing after abphelper generate crud
```
I ran abphelper generate crud for entity [Name].

Review and fix:
1. DbContext: is the DbSet in the right place? Is there stray code?
2. Entity: convert all properties to private set
3. AppService: replace ObjectMapper.Map(input, entity) with entity.Update()
4. Add a static Create factory method
5. Run dotnet build and confirm zero errors
```

## 3. Tuning an EF Core query
```
This query is slow: [the query]

Check:
1. Any N+1? ← add Include/ThenInclude
2. Does it need AsNoTracking? (read-only)
3. Is it SARGable? ← never use YEAR() or functions on columns
4. Any implicit conversion (nvarchar vs varchar)?
5. Does it need a covering index with INCLUDE columns?
```

## 4. Creating an Angular CRUD page
```
Create a management page for [Entity] with Angular + ABP:

- ListComponent: table with pagination + search + filtering + sorting
- FormComponent: modal with a reactive form + validation
- Permission guard
- Localization (Arabic + English)
- trackBy on every ngFor
```
