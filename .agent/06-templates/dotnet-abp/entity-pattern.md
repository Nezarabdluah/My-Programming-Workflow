# .NET ABP Entity Patterns

> Ready-to-copy .NET/ABP and Angular component patterns

---

## Quick Entity Reference

```yaml
EntityName:
  id: Guid
  name: string (300)
  nameAr: string (300)
  isActive: bool
  Relations:
    - BelongsTo: ParentEntity
    - HasMany: ChildEntity
```

---

## DbSets Reference

| DbSet Name | Entity | Table Name |
|------------|--------|------------|
| Users | User | AbpUsers |
| Roles | Role | AbpRoles |

---

## Angular Component Patterns

### List Component Template
```typescript
export class EntityListComponent implements OnInit {
    entities: EntityDto[] = [];
    filterText = '';
    sorting = 'name';
    skipCount = 0;
    maxResultCount = 10;
    totalCount = 0;

    ngOnInit(): void { this.getEntities(); }
    
    getEntities(): void { /* API call with pagination */ }
    create(): void { this.showFormModal(); }
    edit(entity): void { this.showFormModal(entity.id); }
    delete(entity): void { /* confirm + delete */ }
    pageChanged(event): void { /* pagination */ }
    showFormModal(id?): void { /* open modal */ }
}
```

### Form Component Template
```typescript
export class EntityFormComponent {
    @Input() id: number;
    @Output() onSave = new EventEmitter<any>();
    
    saving = false;
    entity: EntityDto = new EntityDto();
    
    ngOnInit(): void {
        if (this.id) { this.loadEntity(); }
    }
    
    save(): void { /* create or update */ }
    close(): void { /* close modal */ }
}
```

---

## Localization Keys

```json
{
  "Create": "Create",
  "Edit": "Edit",
  "Delete": "Delete",
  "Save": "Save",
  "Cancel": "Cancel"
}
```
> (Replace the values with your app's locale labels, e.g. Arabic or French — keys stay in English.)

---

## Layers Flow
```text
Presentation Layer (API / Frontend)
    ↓
Application Layer (Use Cases, Commands, Queries)
    ↓
Domain Layer (Entities, Value Objects, Domain Events, Repository Interfaces)
    ↑
Infrastructure Layer (DbContext, External APIs, Repository Implementations)
```
