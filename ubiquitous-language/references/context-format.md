# CONTEXT.md 格式

## 基本结构

```md
# {上下文名称}

{用一到两句话说明这个上下文是什么，以及为什么存在。}

## Language

**Order**:
{用一到两句话定义这个术语。}
_Avoid_: Purchase, transaction

**Invoice**:
交付后发送给客户的付款请求。
_Avoid_: Bill, payment request

**Customer**:
下达订单的个人或组织。
_Avoid_: Client, buyer, account
```

## 规则

- **立场明确**：多个词指向同一概念时，选择一个标准术语，把其他说法放入 `_Avoid_`。
- **定义要短**：最多一到两句话。说明它是什么，不说明它怎么实现。
- **只写项目特有领域概念**：通用编程概念、工具名、错误类型、技术模式不进入 `CONTEXT.md`。
- **自然分组**：术语出现明显主题聚类时，可以加二级标题；没有必要时保持平铺。
- **不写实现细节**：字段、表结构、接口、类名、技术方案不属于统一语言，除非它们本身就是业务语言。

## 单上下文仓库

多数仓库只需要根目录一个 `CONTEXT.md`：

```text
/
├── CONTEXT.md
└── src/
```

## 多上下文仓库

多个业务上下文并存时，根目录使用 `CONTEXT-MAP.md` 描述上下文位置和关系：

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) - 接收并跟踪客户订单
- [Billing](./src/billing/CONTEXT.md) - 生成发票并处理付款
- [Fulfillment](./src/fulfillment/CONTEXT.md) - 管理拣货和发运

## Relationships

- **Ordering -> Fulfillment**: Ordering 发出 `OrderPlaced` 事件；Fulfillment 消费该事件开始拣货
- **Fulfillment -> Billing**: Fulfillment 发出 `ShipmentDispatched` 事件；Billing 消费该事件生成发票
- **Ordering <-> Billing**: 共享 `CustomerId` 和 `Money` 类型
```

判断规则：

- 如果存在 `CONTEXT-MAP.md`，先读它，再定位具体上下文。
- 如果只有根目录 `CONTEXT.md`，按单上下文处理。
- 如果两者都没有，在第一个术语确认后创建根目录 `CONTEXT.md`。
- 如果多个上下文都可能适用，先问用户，不要猜。
