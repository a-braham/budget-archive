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
