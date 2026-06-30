from collections import Counter
from pathlib import Path
import csv
import re

ROOT = Path(r"research_corpus\Kinetic Economy")
INV = ROOT / "_inventory"
SOURCE_MANIFEST = INV / "source_document_manifest.csv"
OUT_CSV = INV / "evidence_classification_manifest.csv"
OUT_MD = INV / "evidence_classification_summary.md"

FIELDNAMES = [
    "source_doc_id",
    "original_filename",
    "relative_path",
    "file_type",
    "primary_domain",
    "secondary_domains",
    "inferred_source_type",
    "inferred_publisher",
    "inferred_industry",
    "inferred_technology",
    "inferred_capabilities",
    "inferred_business_models",
    "inferred_operating_models",
    "inferred_customer_experience",
    "inferred_frameworks",
    "inferred_output_relevance",
    "classification_confidence",
    "classification_method",
    "review_needed",
    "notes",
]

PRIMARY_DOMAIN_KEYWORDS = {
    "ai": [
        "ai",
        "artificial intelligence",
        "gen ai",
        "gen-ai",
        "generative ai",
        "agentic",
        "llm",
        "machine learning",
        "compute",
    ],
    "adaptability": ["adaptability", "adaptable", "adaptive", "adaptation", "adapting", "disruption", "volatility"],
    "agile": ["agile", "scrum", "sprint"],
    "blockchain": ["blockchain", "web3", "token", "tokenization", "digital asset", "crypto", "rwa"],
    "business_models": ["business model", "business models", "subscription", "freemium", "revenue model"],
    "customer_experience": [
        "customer",
        "consumer",
        "cx",
        "journey",
        "loyalty",
        "omnichannel",
        "ecommerce",
        "e-commerce",
        "retail",
    ],
    "digital_transformation": ["digital transformation", "digitization", "digitalisation", "digitalization", "digital strategy"],
    "dynamic_capabilities": ["dynamic capabilities", "dynamic capability", "resource redeployment", "reconfiguration"],
    "global_digital_policy": ["global", "g20", "oecd", "world bank", "imf", "wef", "wipo", "unesco", "digital policy"],
    "government": ["government", "govt", "public", "national", "ministry", "digital service", "digital government"],
    "innovation": ["innovation", "innovative", "disruptive innovation", "ecosystem value"],
    "marketing_maturity": ["marketing maturity", "digital marketing", "market mix", "earned media", "social media", "go to market"],
    "operating_models": ["operating model", "organization", "organisational", "organizational", "enterprise architecture"],
    "platforms_marketplaces": ["platform", "marketplace", "marketplaces", "ecosystem", "two side", "2 side"],
    "quantum": ["quantum"],
    "technology_infrastructure": ["cloud", "data center", "data centre", "infrastructure", "architecture", "cybersecurity", "iot"],
    "velocity": ["velocity", "speed", "fast", "acceleration", "accelerate"],
    "wine": ["wine", "winery", "vineyard", "terroir"],
}

PUBLISHER_HINTS = {
    "McKinsey": ["mckinsey"],
    "Deloitte": ["deloitte"],
    "BCG": ["bcg", "boston consulting group"],
    "Bain": ["bain"],
    "Accenture": ["accenture"],
    "Capgemini": ["capgemini", "cap gemini"],
    "Gartner": ["gartner"],
    "IBM": ["ibm"],
    "Microsoft": ["microsoft"],
    "Google": ["google"],
    "OpenAI": ["openai"],
    "WEF": ["wef", "world economic forum"],
    "World Bank": ["world bank"],
    "IMF": ["imf"],
    "OECD": ["oecd"],
    "Oxford": ["oxford"],
    "Stanford": ["stanford"],
    "Wharton": ["wharton"],
    "PwC": ["pwc", "pricewaterhousecoopers"],
    "KPMG": ["kpmg"],
    "HBR": ["hbr", "harvard business review"],
    "Statista": ["statista"],
    "MIT": ["mit"],
    "EY": ["ey", "ernst young"],
}

TAG_KEYWORDS = {
    "inferred_capabilities": {
        "adaptability": ["adaptability", "adaptable", "adaptive", "adaptation"],
        "velocity": ["velocity", "speed", "acceleration", "accelerate"],
        "learning": ["learning", "double-loop", "knowledge"],
        "resilience": ["resilience", "resiliance", "resilient"],
        "trust": ["trust", "responsible ai"],
        "innovation": ["innovation", "innovative", "disruptive"],
        "composability": ["composable", "composability", "modularity", "modular"],
        "agility": ["agile", "agility"],
        "decision_making": ["decision", "decisions"],
        "customer_intelligence": ["customer intelligence", "consumer insights", "cdp", "attribution"],
        "ai_readiness": ["ai readiness", "readiness"],
        "organizational_design": ["organization", "organisation", "organizational", "organisational", "culture"],
        "resource_reallocation": ["resource allocation", "resource reallocation", "resource redeployment"],
        "psychological_safety": ["psychological safety"],
        "future_readiness": ["future readiness", "future of", "foresight", "trends", "trend report"],
    },
    "inferred_technology": {
        "artificial_intelligence": ["ai", "artificial intelligence", "machine learning", "generative ai", "gen ai"],
        "agentic_ai": ["agentic", "ai agents", "agent"],
        "blockchain": ["blockchain", "web3"],
        "cloud": ["cloud"],
        "crm": ["crm", "customer relationship"],
        "analytics": ["analytics", "index", "measurement", "metrics", "attribution"],
        "digital_identity": ["digital identity", "identity management"],
        "payments": ["payments", "payment"],
        "quantum": ["quantum"],
        "iot": ["iot", "internet of things"],
        "automation": ["automation", "automated"],
        "cybersecurity": ["cybersecurity", "cyber security"],
    },
    "inferred_business_models": {
        "subscription": ["subscription"],
        "marketplace": ["marketplace", "marketplaces"],
        "platform": ["platform"],
        "freemium": ["freemium"],
        "advertising": ["advertising", "ad effectiveness", "media"],
        "membership": ["membership"],
        "cloud": ["cloud", "saas"],
        "open_source": ["open source"],
        "sharing_economy": ["sharing economy"],
        "ecosystem": ["ecosystem"],
        "tokenization": ["tokenization", "tokenomics", "token"],
    },
    "inferred_operating_models": {
        "agile": ["agile"],
        "platform_team": ["platform team"],
        "product_team": ["product team", "product operating"],
        "unification": ["unification"],
        "coordination": ["coordination", "orchestration"],
        "replication": ["replication"],
        "diversification": ["diversification"],
        "ai_native": ["ai native", "ai-native", "agentic"],
        "networked": ["networked", "ecosystem", "network"],
    },
    "inferred_customer_experience": {
        "website": ["website", "web strategy"],
        "mobile": ["mobile"],
        "ecommerce": ["ecommerce", "e-commerce", "commerce"],
        "omnichannel": ["omnichannel", "omni-channel"],
        "email": ["email"],
        "sms": ["sms"],
        "push": ["push"],
        "social": ["social"],
        "content": ["content"],
        "loyalty": ["loyalty"],
        "customer_service": ["customer service", "service"],
        "personalization": ["personalization", "personalisation"],
        "ai_agent": ["ai agent", "ai agents", "agentic"],
    },
    "inferred_output_relevance": {
        "kinetic_organization": ["kinetic", "adaptive", "dynamic capabilities", "velocity", "resilience"],
        "overclocked": ["overclocked", "velocity", "acceleration", "future readiness"],
        "web_strategy_course": ["website", "web strategy", "ecommerce", "digital marketing", "customer journey", "omnichannel"],
        "mba_digital_strategy": ["digital strategy", "business model", "digital transformation", "executive", "ceo"],
        "cinaptic": ["cinaptic"],
        "government_as_a_service": ["government", "digital government", "digital service", "govt", "public"],
        "terroir_os": ["wine", "winery", "vineyard", "terroir"],
        "writing": ["writing", "framework", "playbook", "guide", "case study"],
    },
}

INDUSTRY_KEYWORDS = {
    "advertising_media_marketing": ["advertising", "media", "marketing", "social media", "earned media"],
    "banking_finance_insurance": ["banking", "finance", "financial", "insurance", "fintech", "payments"],
    "consumer_retail_ecommerce": ["consumer", "retail", "ecommerce", "e-commerce", "commerce", "cpg"],
    "government_public_sector": ["government", "govt", "public", "national", "ministry"],
    "technology_saas_platforms": ["technology", "saas", "software", "platform", "cloud"],
    "manufacturing_industrial": ["manufacturing", "industry 4.0", "industrial"],
    "wine_hospitality": ["wine", "winery", "vineyard", "terroir", "hospitality", "hotel", "hilton"],
    "smart_cities": ["smart city", "smart cities"],
    "sports_entertainment": ["sports", "gaming", "warner bros", "lotr", "entertainment"],
    "education_research": ["academic", "university", "journal", "research"],
}

FRAMEWORK_KEYWORDS = {
    "dynamic_capabilities": ["dynamic capabilities", "dynamic capability", "teece"],
    "ai_adoption_maturity": ["ai adoption maturity", "ai maturity"],
    "digital_maturity_model": ["digital maturity", "maturity model"],
    "business_model_canvas": ["business model"],
    "adaptive_leadership": ["adaptive leadership"],
    "elements_of_value": ["elements of value"],
    "marketplace_design": ["marketplace", "designing markets"],
    "enterprise_architecture": ["enterprise architecture"],
    "agile_at_scale": ["agile at scale"],
}

DUPLICATE_HINTS = [" copy", "- copy", "(1)", "(2)", "duplicate", "final final"]


def normalize(value):
    value = value.lower()
    value = re.sub(r"[_\-]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def keyword_matches(text, keywords):
    matches = []
    padded = f" {text} "
    for keyword in keywords:
        needle = normalize(keyword)
        if len(needle) <= 3:
            if re.search(rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])", padded):
                matches.append(keyword)
        elif needle in text:
            matches.append(keyword)
    return matches


def infer_domains(text):
    scores = Counter()
    for domain, keywords in PRIMARY_DOMAIN_KEYWORDS.items():
        matches = keyword_matches(text, keywords)
        if matches:
            scores[domain] = len(matches)

    if not scores:
        return "other", []

    ordered = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    return ordered[0][0], [domain for domain, _ in ordered[1:]]


def infer_publisher(text):
    for publisher, hints in PUBLISHER_HINTS.items():
        if keyword_matches(text, hints):
            return publisher
    return "unknown"


def infer_source_type(text, publisher):
    consulting_publishers = {"McKinsey", "Deloitte", "BCG", "Bain", "Accenture", "Capgemini", "PwC", "KPMG", "EY"}
    government_publishers = {"WEF", "World Bank", "IMF", "OECD"}
    academic_publishers = {"Oxford", "Stanford", "Wharton", "MIT"}

    if keyword_matches(text, ["academic", "journal", "research", "university", "paper", "study"]):
        return "academic"
    if publisher in consulting_publishers:
        return "consulting"
    if publisher in government_publishers or keyword_matches(text, ["government", "govt", "ministry", "national", "oecd", "imf", "world bank"]):
        return "government"
    if keyword_matches(text, ["annual report", "company report", "10-k", "investor"]):
        return "company_report"
    if keyword_matches(text, ["report", "trend", "trends", "index", "survey", "whitepaper", "white paper"]):
        return "industry_report"
    if publisher == "HBR" or keyword_matches(text, ["hbr", "playbook", "guide", "case study", "checklist"]):
        return "practitioner"
    if keyword_matches(text, ["task assessment", "group analysis", "chapter"]):
        return "internal"
    if publisher in academic_publishers:
        return "academic"
    return "unknown"


def infer_tags(text, tag_map):
    tags = []
    for tag, keywords in tag_map.items():
        if keyword_matches(text, keywords):
            tags.append(tag)
    return tags


def join_tags(tags):
    return ";".join(tags)


def confidence(primary_domain, publisher, source_type, tag_count):
    if publisher != "unknown" or primary_domain != "other":
        if publisher != "unknown" and primary_domain != "other":
            return "high"
        if source_type != "unknown" and primary_domain != "other":
            return "high"
    if tag_count >= 3 or source_type != "unknown":
        return "medium"
    return "low"


def classify(row):
    filename = row["original_filename"]
    rel_path = row["relative_path"]
    file_type = row["file_type"]
    text = normalize(f"{filename} {rel_path}")

    primary_domain, secondary_domains = infer_domains(text)
    publisher = infer_publisher(text)
    source_type = infer_source_type(text, publisher)
    industry = infer_tags(text, INDUSTRY_KEYWORDS)
    frameworks = infer_tags(text, FRAMEWORK_KEYWORDS)

    tag_results = {
        field: infer_tags(text, tag_map)
        for field, tag_map in TAG_KEYWORDS.items()
    }
    tag_count = sum(len(tags) for tags in tag_results.values()) + len(industry) + len(frameworks)
    classification_confidence = confidence(primary_domain, publisher, source_type, tag_count)

    no_extension = not file_type
    duplicate_hint = any(hint in text for hint in DUPLICATE_HINTS)
    review_needed = (
        primary_domain == "other"
        or source_type == "unknown"
        or classification_confidence == "low"
        or no_extension
        or duplicate_hint
    )

    notes = []
    if no_extension:
        notes.append("filename_has_no_extension")
    if duplicate_hint:
        notes.append("duplicate_or_copy_indicator")
    if primary_domain == "other":
        notes.append("no_primary_domain_filename_match")
    if source_type == "unknown":
        notes.append("no_source_type_filename_match")

    return {
        "source_doc_id": row["source_doc_id"],
        "original_filename": filename,
        "relative_path": rel_path,
        "file_type": file_type,
        "primary_domain": primary_domain,
        "secondary_domains": join_tags(secondary_domains),
        "inferred_source_type": source_type,
        "inferred_publisher": publisher,
        "inferred_industry": join_tags(industry),
        "inferred_technology": join_tags(tag_results["inferred_technology"]),
        "inferred_capabilities": join_tags(tag_results["inferred_capabilities"]),
        "inferred_business_models": join_tags(tag_results["inferred_business_models"]),
        "inferred_operating_models": join_tags(tag_results["inferred_operating_models"]),
        "inferred_customer_experience": join_tags(tag_results["inferred_customer_experience"]),
        "inferred_frameworks": join_tags(frameworks),
        "inferred_output_relevance": join_tags(tag_results["inferred_output_relevance"]),
        "classification_confidence": classification_confidence,
        "classification_method": "filename_and_metadata_heuristics_v1",
        "review_needed": str(review_needed).lower(),
        "notes": ";".join(notes),
    }


def count_split_tags(rows, field):
    counts = Counter()
    for row in rows:
        for tag in row[field].split(";"):
            if tag:
                counts[tag] += 1
    return counts


def write_count_section(handle, title, counts, limit=None):
    handle.write(f"## {title}\n\n")
    items = counts.most_common(limit) if limit else sorted(counts.items())
    if not items:
        handle.write("- none: 0\n")
    else:
        for key, count in items:
            handle.write(f"- {key}: {count}\n")
    handle.write("\n")


def main():
    with open(SOURCE_MANIFEST, newline="", encoding="utf-8") as f:
        rows = [classify(row) for row in csv.DictReader(f)]

    if not rows:
        raise ValueError("No source documents found to classify.")

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    domain_counts = Counter(row["primary_domain"] for row in rows)
    source_type_counts = Counter(row["inferred_source_type"] for row in rows)
    publisher_counts = Counter(row["inferred_publisher"] for row in rows)
    review_count = sum(1 for row in rows if row["review_needed"] == "true")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("# Evidence Classification Summary\n\n")
        f.write("Classification method: filename_and_metadata_heuristics_v1\n\n")
        f.write(f"Total source documents classified: {len(rows)}\n\n")
        f.write(f"Requiring review: {review_count}\n\n")
        write_count_section(f, "Counts by Primary Domain", domain_counts)
        write_count_section(f, "Counts by Inferred Source Type", source_type_counts)
        write_count_section(f, "Counts by Inferred Publisher", publisher_counts)
        write_count_section(f, "Top 20 Capability Tags", count_split_tags(rows, "inferred_capabilities"), 20)
        write_count_section(f, "Top 20 Technology Tags", count_split_tags(rows, "inferred_technology"), 20)
        write_count_section(f, "Top 20 Output Relevance Tags", count_split_tags(rows, "inferred_output_relevance"), 20)

    print(f"Evidence classification manifest written to: {OUT_CSV}")
    print(f"Summary written to: {OUT_MD}")


if __name__ == "__main__":
    main()
