CREATE_USER = """
mutation CreateUser(
  $email: String!, $username: String!,
  $phone_number: String!, $first_name: String!,
  $last_name: String!, $password: String!
  ){ register(
    email: $email,
    username: $username,
    phoneNumber: $phone_number,
    firstName: $first_name,
    lastName: $last_name,
    password: $password
  ) {
    user {
      username,
      email,
      phoneNumber,
      firstName,
      middleName,
      lastName,
      isActive,
      isVerified,
    }
  }
}
"""

CREATE_MUTATION = """
mutation CreateAccount($name: String!, $institution: String!, $type: String!, $number: String!){
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
        phoneNumber
      }
    }
  }
}
"""

UPDATE_MUTATION = """
mutation EditAccount($id: ID!, $name: String!, $institution: String!, $type: String!, $number: String!){
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
        email,
        phoneNumber
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
mutation CreateTransaction($account: ID!, $reference: String!, $type: String!, $amount: Decimal!){
  createTransaction(
    accountId: $account,
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
        email,
        phoneNumber
      }
    }
  }
}
"""
UPDATE_TRANSACTION = """
mutation UpdateTransaction($id: ID!, $reference: String!, $type: String!, $amount: Decimal!){
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
        email,
        phoneNumber
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
