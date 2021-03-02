CREATE_USER = """
mutation CreateUser(
  $email: String!, $username: String!, $password: String!
  ){ register(
    email: $email,
    username: $username,
    password: $password
  ) {
    user {
      username,
      email,
      isActive,
      isVerified,
    }
  }
}
"""

CREATE_MUTATION = """
mutation CreateAccount(
  $name: String!, $institution: String!, $type: String!, $number: String!
  ){
  createAccount(
    accountData: {
      name: $name, institution: $institution, type: $type, number: $number
      }
    ){
    success
    account {
      name,
      institution,
      type,
      amount,
      number,
      description,
      user {
        id,
        username,
        email,
      }
    }
  }
}
"""

UPDATE_MUTATION = """
mutation EditAccount(
  $id: ID!, $name: String!, $institution: String!,
  $type: String!, $number: String!
  ){
  editAccount(
    id: $id,
    accountData: {
      name: $name, institution: $institution, type: $type, number: $number
      }
    ){
    success
    account {
      name,
      institution,
      type,
      amount,
      number,
      description,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""

ONE_ACCOUNT = """
query QueryAccount($id: ID!, $number: String!){
  account(id: $id) {
      name
  }
  otherDetails: account(accountNumber: $number) {
      institution
      type
      amount,
  }
}
"""

ALL_ACCOUNTS = """
query {
  allAccounts {
    id,
    name
  }
}
"""

CREATE_TRANSACTION = """
mutation CreateTransaction(
  $from_account: ID!, $to_account: ID!,
  $reference: String!, $type: String!, $amount: Decimal!
  ){
  createTransaction(
    fromId: $from_account,
    toId: $to_account,
    transactionData: {
      reference: $reference, type: $type, amount: $amount
      }
    ){
    success
    transaction {
      reference,
      type,
      amount,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""
UPDATE_TRANSACTION = """
mutation UpdateTransaction(
  $id: ID!, $reference: String!, $type: String!, $amount: Decimal!
  ){
  updateTransaction(
    transactionId: $id,
    transactionData: {
      reference: $reference, type: $type, amount: $amount
      }
    ){
    success
    transaction {
      reference,
      type,
      amount,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""
ONE_TRANSACTION = """
query QueryTransaction($id: ID!, $reference: String!){
  transaction(transactionId: $id) {
      reference
  }
  otherDetails: transaction(transactionReference: $reference) {
      type
      amount,
  }
}
"""
ALL_TRANSACTIONS = """
query {
  allTransactions {
    id,
    reference
  }
}
"""

CREATE_CATEGORY = """
mutation CreateCategory($name: String!, $type: String!, $description: String!){
  createCategory(
    categoryData: {
      name: $name, type: $type, description: $description
      }
    ){
    success
    category {
      name,
      type,
      description,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""
UPDATE_CATEGORY = """
mutation UpdateCategory($id: ID!, $name: String!, $type: String!){
  updateCategory(
    id: $id,
    categoryData: {
      name: $name, type: $type
      }
    ){
    success
    category {
      name,
      type,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""
ONE_CATEGORY = """
query QueryCategory($id: ID!){
  category(id: $id) {
      name,
      type
  }
}
"""
ALL_CATEGORIES = """
query {
  allCategories {
    id,
    name,
    type
  }
}
"""

CREATE_BUDGET = """
mutation CreateBudget($category: ID!, $amount: Decimal!){
  createBudget(
    categoryId: $category,
    budgetData: {
      amount: $amount
      }
    ){
    success
    budget {
      id,
      amount,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""
UPDATE_BUDGET = """
mutation UpdateBudget($id: ID!, $amount: Decimal!){
  updateBudget(
    budgetId: $id,
    budgetData: {
      amount: $amount
      }
    ){
    success
    budget {
      id,
      amount,
      user {
        id,
        username,
        email
      }
    }
  }
}
"""
ONE_BUDGET = """
query QueryBudget($id: ID!){
  budget(budgetId: $id) {
      id,
      amount
  }
}
"""
ALL_BUDGETS = """
query {
  allBudgets {
    id,
    amount
  }
}
"""
