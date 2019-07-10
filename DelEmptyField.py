#!/usr/bin/env python3
# __author__ = Yang Xiao


def del_empty_field(obj: [dict, list], parent=None, key_in_parent=None):
    """
    递归删除空值（包括长度为 0 的 dict、list，以及去除前后空格后长度为 0 的 str，以及 None）
    :param obj: 输入
    :param parent: 不要手动干预这个参数，递归过程会自动设置该参数
    :param key_in_parent: 不要手动干预这个参数，递归过程会自动设置该参数
    :return: 方法没有返回值，直接修改输入参数本身
    """
    if type(obj) == dict:
        _dict = obj
        for k in list(_dict.keys()):
            v = _dict[k]
            if isinstance(v, str):
                if v is None or not len(v.strip()):
                    del _dict[k]
            elif isinstance(v, list):
                del_empty_field(v, _dict, k)
            elif isinstance(v, dict):
                del_empty_field(v, _dict, k)
            elif v is None:
                del _dict[k]

    elif type(obj) == list:
        for index in range(len(obj) - 1, -1, -1):
            it = obj[index]
            if isinstance(it, dict) or isinstance(it, list):
                del_empty_field(it, obj)

    if not len(obj) and parent is not None:
        if type(parent) == dict:
            if key_in_parent is not None:
                del parent[key_in_parent]
        elif type(parent) == list:
            parent.remove(obj)
        else:
            raise Exception(type(parent))


if __name__ == '__main__':
    mock_data = {
        "_class": "org.scbit.lsbi.mcp.pojo.mongo.microbe.AuditResult",
        "audit_task_detail_id": "RBVMA7AAF5G2RGKBRPGRAR65HA",
        "audit_task_id": "BDISRZTUABFVHHHE7ZVHTYA2Q4",
        "audit_task_record_id": "N4BJEI27WJCENLPQRS2ET56I3M",
        "pmid": 8573508,
        "lmsg_id": "MSGB_myco_001238",
        "type": "审编数据",
        "status": "normal",
        "pdf_path": "attachment/3a/d8/D18K3KOo6Fl5oFbY.pdf",
        "auditor": "7BVUZR2R2BDHPJRS3O4KKLCRPA",
        "creator": "7BVUZR2R2BDHPJRS3O4KKLCRPA",
        "editor": "7BVUZR2R2BDHPJRS3O4KKLCRPA",
        "dict": {
            "name": "eLMSG_biocuration",
            "abbreviation": "eLMSG_biocuration",
            "data": {
                "Name": "Mycobacterium intracellulare",
                "LMSG_ID": "MSGB_myco_001238",
                "DOI": "10.1099/00207713-46-1-280",
                "Title": "Semantide- and Chemotaxonomy-Based Analyses of Some Problematic Phenotypic Clusters of Slowly Growing Mycobacteria, a Cooperative Study of the International Working Group on Mycobacterial Taxonomy",
                "Rank": "Strain",
                "Strain": "IWGMT 90248",
                "Isolation and sampling": [
                    {}
                ],
                "Environmental Information": [
                    {}
                ],
                "Growth rate": "slowly growing",
                "size": [
                    {}
                ],
                "Multicellular morphology": [
                    {}
                ],
                "Colony Morphology": [
                    {
                        "Medium compo": [
                            {}
                        ]
                    }
                ],
                "Nitrate Reduction": "false",
                "C/N source": [
                    {
                        "Metabolite": "Tween (10-d)",
                        "Ability": "negative"
                    }
                ],
                "GC": [
                    {}
                ],
                "Temperature": [
                    {
                        "range": "25.0 ℃",
                        "ability": "positive"
                    }
                ],
                "pH": [
                    {}
                ],
                "Metabolite production": [
                    {}
                ],
                "Composition": [
                    {}
                ],
                "Halophily": [
                    {}
                ],
                "Tolerance": [
                    {
                        "Compound name": "Ethambutol",
                        "Concentration": "1.00 &mu;g/ml"
                    },
                    {
                        "Compound name": "Hydroxylamine",
                        "Concentration": "125.00 &mu;g/ml"
                    },
                    {
                        "Compound name": "Oleate",
                        "Concentration": "250.00 &mu;g/ml"
                    },
                    {
                        "Compound name": "p-Nitrobenzoate",
                        "Concentration": "500.00 &mu;g/ml"
                    },
                    {
                        "Compound name": "Thiophene-2-carboxylic acid hydrazide",
                        "Concentration": "1.00 &mu;g/ml"
                    }
                ],
                "Antibiotic": [
                    {
                        "metabolite": "Isoniazid",
                        "concentration": "1.0 &mu;g/ml",
                        "value": "resistant"
                    },
                    {
                        "metabolite": "Thiacetazone",
                        "concentration": "10.0 &mu;g/ml",
                        "value": "resistant"
                    }
                ],
                "Fatty acids detail": [
                    {}
                ],
                "Enzym": [
                    {
                        "enzyme": "Nicotinamidase",
                        "activity": "+"
                    },
                    {
                        "enzyme": "Urease",
                        "activity": "-"
                    },
                    {
                        "enzyme": "Arylsulfatase (10-d)",
                        "activity": "-"
                    },
                    {
                        "enzyme": "Catalase (68&deg;C)",
                        "activity": "+"
                    },
                    {
                        "enzyme": "Alpha-esterase",
                        "activity": "+"
                    },
                    {
                        "enzyme": "Beta-galactosidase",
                        "activity": "-"
                    },
                    {
                        "enzyme": "Acidphosphatase",
                        "activity": "-"
                    }
                ]
            }
        },
        "click": [
            "eLMSGB180",
            "eLMSGB79",
            "eLMSGB180",
            "eLMSGB180",
            "eLMSGB180",
            "eLMSGB180",
            "eLMSGB184",
            "eLMSGB26",
            "eLMSGB197",
            "eLMSGB45",
            "eLMSGB58",
            "eLMSGB48",
            "eLMSGB48",
            "eLMSGB45",
            "eLMSGB58",
            "eLMSGB190",
            "eLMSGB126",
            "eLMSGB180",
            "eLMSGB180"
        ],
        "最深空数组": [
            {"v": {
                "c": {
                    "e": [],
                    "q": {
                        "ee": {
                            "vv": [
                                {"aaa": [
                                    {"aaa": []}
                                ]}
                            ]
                        }
                    }
                }
            }},
            {"v": {
                "c": {
                    "e": []
                }
            }},
        ],
        "最深非空数组": [
            {"v": {
                "c": {
                    "e": [],
                    "q": {
                        "ee": {
                            "vv": [
                                {"aaa": [
                                    {"aaa": ["这里是不会被删掉的"]}
                                ]}
                            ]
                        }
                    }
                }
            }},
            {"v": {
                "c": {
                    "e": []
                }
            }},
        ]
    }

    # 这个方法不能接受返回值，不需要 return
    del_empty_field(mock_data)

    if len(mock_data) == 0:
        pass
        # 整个都是空

    import json

    print(json.dumps(mock_data, indent=2, ensure_ascii=False))
