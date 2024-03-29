{
    "configuration": {
        "interfaces": {
            "interface": [
                {
                    "@": {"protect": True},
                    "name": "ge-0/0/0",
                    "unit": [
                        {
                            "name": 0,
                            "family": {
                                "inet": {"address": [{"name": "198.51.100.1/24"}]}
                            },
                        }
                    ],
                }
            ]
        }
    },
    "ospf-neighbor-information": [
        {
            "neighbor-address": "192.168.1.1",
            "interface-name": "ge-0/0/1.1",
            "ospf-neighbor-state": "Full",
            "neighbor-id": "10.0.0.2",
            "neighbor-priority": "128",
            "activity-timer": "38",
        },
        {
            "neighbor-address": "192.168.4.1",
            "interface-name": "ge-0/0/1.4",
            "ospf-neighbor-state": "Full",
            "neighbor-id": "10.0.0.4",
            "neighbor-priority": "128",
            "activity-timer": "35",
        },
    ],
}
