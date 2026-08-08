from app.services.comparison_builder import (
    build_company_comparison,
)

from app.services.comparison_prompt import (
    build_comparison_prompt,
)

from app.services.gemini_service import (
    generate_research,
)


def compare_companies(companies):
    """
    Generate an AI comparison report for multiple companies.
    """

    # ---------------------------------
    # Build Live Comparison Data
    # ---------------------------------
    comparison = build_company_comparison(companies)

    # ---------------------------------
    # Build AI Prompt
    # ---------------------------------
    prompt = build_comparison_prompt(comparison)

    # ---------------------------------
    # Generate AI Report
    # ---------------------------------
    report = generate_research(prompt)

    return {
        "companies": comparison,
        "report": report,
    }