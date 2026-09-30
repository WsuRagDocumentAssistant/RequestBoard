from dataclasses import dataclass, replace
from typing import Any

# 처리 상태. 접수 / 검토 중 / 반영 완료 / 반려
STATUSES = ("received", "in_progress", "done", "rejected")


@dataclass
class FeatureRequest:
    """기능 개선 요청 글 하나를 담는 객체. DB에서 온 값을 형태 그대로 담는다."""

    id: Any              # 글 번호
    title: str           # 제목
    content: Any         # 내용 (가려지면 None)
    is_secret: bool      # 비밀글 여부
    author_id: Any       # 작성자 user_id
    author_name: str     # 작성자 이름
    created_at: Any      # 작성 시각
    status: str          # 처리 상태 (STATUSES 중 하나)
    answer: Any = None       # 관리자 답변
    answered_at: Any = None  # 답변 시각

    def can_view(self, user_id, is_admin) -> bool:
        """공개글이거나, 관리자이거나, 작성자 본인이면 내용을 볼 수 있다."""
        return not self.is_secret or is_admin or str(self.author_id) == str(user_id)

    def for_user(self, user_id, is_admin) -> "FeatureRequest":
        """볼 수 없는 비밀글이면 제목·내용·답변을 비운 사본을, 아니면 그대로 돌려준다."""
        if self.can_view(user_id, is_admin):
            return self
        return replace(self, title="", content=None, answer=None)
