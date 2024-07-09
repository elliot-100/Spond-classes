"""Main module.

```mermaid

erDiagram
    GROUP {
        str uid PK
        inner_obj ROLE
        inner_obj SUBGROUP
        inner_obj MEMBER
    }
    MEMBER {
        str uid PK
        str subgroup_uid FK
        str role_uid FK
        obj profile "?"
    }
    ROLE {
        str uid PK
    }
    SUBGROUP {
        str uid PK
    }
    PROFILE {
        str uid PK
        obj member "?"
    }
    EVENT {
        str uid PK
        inner_obj responses
        inner_obj recipients
    }
    EVENT-RECIPIENT {
        str uid FK "GROUP | SUBGROUP | MEMBER"

    }
    EVENT-RESPONSE {
        str accepted_uids FK "MEMBER"
        str declined_uids FK "MEMBER"
        str unanswered_uids FK "MEMBER"
        str waiting_list_uids FK "MEMBER"
        str unconfirmed_uids FK "MEMBER"
    }

    GROUP 1..0+ ROLE : contains
    GROUP 1..0+ MEMBER : contains
    GROUP 1..0+ SUBGROUP : contains
    GROUP 1..0+ EVENT : owns

    EVENT 1..1 EVENT-RESPONSE : has
    EVENT 1..1 EVENT-RECIPIENT : has

    MEMBER 1..zero or one PROFILE : has
    MEMBER 1..0+ ROLE : has
    MEMBER 1..0+ SUBGROUP : has

    EVENT-RECIPIENT 1..0+ MEMBER : contains
    EVENT-RECIPIENT 1..0+ GROUP: has
    EVENT-RECIPIENT 1..0+ SUBGROUP: has

    EVENT-RESPONSE 1..0+ MEMBER : contains
```

"""

# Explicitly import all classes and functions into the package namespace.

from .event import Event, EventType
from .group import Group
from .member import Member
from .role import Role
from .subgroup import Subgroup

__all__ = [
    "Event",
    "EventType",
    "Group",
    "Member",
    "Role",
    "Subgroup",
]
