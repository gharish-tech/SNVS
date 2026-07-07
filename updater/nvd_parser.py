def parse_cves(data):

    parsed = []

    vulnerabilities = data.get("vulnerabilities", [])

    for item in vulnerabilities:

        cve = item.get("cve", {})

        # ----------------------------
        # Description
        # ----------------------------

        descriptions = cve.get("descriptions", [])

        description = ""

        if descriptions:
            description = descriptions[0].get("value", "")

        # ----------------------------
        # CVSS
        # ----------------------------

        severity = "Unknown"
        cvss = 0.0

        metrics = cve.get("metrics", {})

        if "cvssMetricV31" in metrics:

            metric = metrics["cvssMetricV31"][0]

            severity = metric["cvssData"]["baseSeverity"]
            cvss = metric["cvssData"]["baseScore"]

        elif "cvssMetricV30" in metrics:

            metric = metrics["cvssMetricV30"][0]

            severity = metric["cvssData"]["baseSeverity"]
            cvss = metric["cvssData"]["baseScore"]

        elif "cvssMetricV2" in metrics:

            metric = metrics["cvssMetricV2"][0]

            severity = metric["baseSeverity"]
            cvss = metric["cvssData"]["baseScore"]

        # ----------------------------
        # Product + Version
        # ----------------------------

        product = ""
        version_start = ""
        version_end = ""

        configurations = cve.get("configurations", [])

        if configurations:

            nodes = configurations[0].get("nodes", [])

            if nodes:

                cpe_matches = nodes[0].get("cpeMatch", [])

                if cpe_matches:

                    criteria = cpe_matches[0].get("criteria", "")

                    parts = criteria.split(":")

                    if len(parts) > 5:

                        product = parts[4]

                    version_start = cpe_matches[0].get(
                        "versionStartIncluding", ""
                    )

                    version_end = cpe_matches[0].get(
                        "versionEndIncluding", ""
                    )

                    if version_end == "":
                        version_end = parts[5]

        parsed.append({

            "id": cve.get("id"),

            "product": product,

            "versionStart": version_start,

            "versionEnd": version_end,

            "severity": severity,

            "cvss": cvss,

            "description": description,

            "published": cve.get("published"),

            "lastModified": cve.get("lastModified")

        })

    return parsed
