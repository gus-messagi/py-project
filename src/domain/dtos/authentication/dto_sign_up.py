from pydantic import BaseModel, Field, model_validator

class SignUpDto(BaseModel):
  name: str
  phone: str
  password: str = Field(min_length=6)
  confirm_password: str = Field(min_length=6)

  @model_validator(mode="after")
  def check_passwords_match(self) -> 'SignUpDto':
    pw1 = self.password
    pw2 = self.confirm_password

    if pw1 is not None and pw2 is not None and pw1 != pw2:
      raise ValueError('passwords do not match')
    
    return self