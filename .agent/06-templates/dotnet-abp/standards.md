# .NET ABP Standards — .NET/ABP-Specific Standards

> Template dedicated to .NET 8 + ABP Framework + SQL Server + Angular

---

## Entity Rules

### The Encapsulation Rule — private set always
1. Every property in an Entity must end with `private set;`
2. As soon as `abphelper` finishes generating the CRUD, immediately fix the `AppService`
3. Using `ObjectMapper.Map(input, entity)` in update operations is forbidden

### The approved pattern:
```csharp
// In the Application Service
public async Task<EntityDto> UpdateAsync(Guid id, UpdateEntityDto input)
{
    var entity = await _repository.GetAsync(id);
    entity.Update(input.Name, input.Slug);
    return ObjectMapper.Map<Entity, EntityDto>(entity);
}
```

### Entity inheritance:
- ✅ Inherit from `FullAuditedAggregateRoot<Guid>` for audit tracking (create, edit, delete)
- ✅ Use `private setters` for encapsulation
- ✅ Use a `static Create` method as the only way to construct the object
- ✅ Use `Check.NotNullOrWhiteSpace` for validation

---

## DDD in ABP

### Domain Events vs Integration Events:
- **Domain Event**: raised inside the Bounded Context
- **Integration Event**: raised across the Message Bus to external systems

### Value Objects:
- ✅ Use `public readonly record struct` to guarantee immutability

### Bounded Contexts:
- Context boundaries are drawn where meaning differs (Ubiquitous Language)

---

## System Internals

### WAL & CDC:
- The DB writes to the Write-Ahead Log first (Sequential I/O), then moves data to tables
- For data movement: use CDC (e.g. Debezium) instead of periodic SELECT polling

### API Gateway (YARP / ABP):
- **Rate Limiting**: Token Bucket → 429 Too Many Requests
- **Load Balancing**: Round Robin or Least Connections

---

## AbpHelper Warning

> ⚠️ After every `abphelper generate crud`:

1. Open `DbContext` immediately and verify:
   - `DbSet<Entity>` is in the right place
   - No stray `builder.Entity` code in the DbSets section
   - No syntax errors
2. Run `dotnet build` before any Migration

---

## Async Everywhere:
- ✅ Every DB operation must be asynchronous
- ❌ Never block on async methods synchronously

## Caching Strategy:
- ✅ Cache lookups (countries, cities): 5-15 minutes
- ✅ Response caching for public GET endpoints

## Frontend (Angular):
- ✅ `trackBy` in every list rendering
- ✅ Use a change detection strategy
- ✅ Server-side filtering — never filter large arrays in the browser
