from .request import FeatureRequest


def build_request(row):
    """DB에서 꺼내온 행(dict)을 받아 FeatureRequest 객체로 만들어 반환한다.

    값은 변환하지 않고 들어온 형태 그대로 담는다.
    """
    return FeatureRequest(
        id=row["id"],
        title=row["title"],
        content=row["content"],
        is_secret=row["is_secret"],
        author_id=row["author_id"],
        author_name=row["author_name"],
        created_at=row["created_at"],
        status=row["status"],
        answer=row.get("answer"),
        answered_at=row.get("answered_at"),
    )
