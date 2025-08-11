from pydantic import BaseModel, Field


class AttachmentBase(BaseModel):
    type: str = Field(..., examples=["image"])
    filename: str = Field(..., examples=["example.jpg"])


class AttachmetCreate(AttachmentBase):
    message_id: int = Field(..., examples=[1])


class  AttachmentsResponse(AttachmentBase):
    id: int
    url: str = Field(..., examples=['s3://images/photo1.jpg'])

    class Config:
        from_attributes = True
