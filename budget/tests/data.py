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
