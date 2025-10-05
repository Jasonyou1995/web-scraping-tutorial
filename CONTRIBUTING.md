# Contributing to Web Scraping Tutorial

Thank you for your interest in contributing! 🎉

This document provides guidelines for contributing to the Web Scraping Tutorial.

## Ways to Contribute

### 1. Report Issues

Found a bug or error?
- Check if it's already reported
- Create a detailed issue with:
  - Clear description
  - Steps to reproduce
  - Expected vs actual behavior
  - Environment details

### 2. Improve Documentation

- Fix typos or unclear explanations
- Add examples or clarifications
- Improve code comments
- Create diagrams or visualizations

### 3. Add Examples

- Create new code examples
- Add real-world use cases
- Provide alternative solutions
- Include edge cases

### 4. Create Exercises

- Design practice problems
- Add progressive challenges
- Include solutions with explanations
- Cover different difficulty levels

### 5. Update Dependencies

- Keep libraries up to date
- Test compatibility
- Update documentation
- Note breaking changes

## Getting Started

### Setup Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/web-scraping-tutorial.git
cd web-scraping-tutorial

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a new branch
git checkout -b feature/your-feature-name
```

### Project Structure

```
web-scraping-tutorial/
├── modules/              # Tutorial modules
│   ├── 01_introduction/
│   │   ├── README.md    # Module overview
│   │   ├── tutorial.md  # Detailed tutorial
│   │   ├── examples/    # Code examples
│   │   ├── exercises/   # Practice problems
│   │   └── solutions/   # Exercise solutions
│   └── ...
├── data/                # Sample data
├── utils/               # Utility functions
├── resources/           # Reference materials
└── requirements.txt     # Dependencies
```

## Contribution Guidelines

### Code Style

**Python Code:**
- Follow PEP 8
- Use descriptive variable names
- Add docstrings to functions
- Include type hints where helpful
- Keep functions focused and small

```python
def extract_product_name(product_element: BeautifulSoup) -> str:
    """
    Extract product name from product element.
    
    Args:
        product_element: BeautifulSoup element containing product
        
    Returns:
        Product name as string
    """
    name_elem = product_element.find('h3', class_='product-name')
    return name_elem.get_text().strip() if name_elem else ""
```

**Markdown:**
- Use clear headings
- Include code blocks with language
- Add examples and screenshots
- Keep explanations concise
- Use bullet points for lists

### Adding Examples

When adding code examples:

1. **Include comments**
   ```python
   # Fetch the webpage
   response = requests.get(url)
   
   # Parse HTML content
   soup = BeautifulSoup(response.content, 'html.parser')
   ```

2. **Make it runnable**
   - Include all imports
   - Provide sample data or URLs
   - Handle errors gracefully

3. **Keep it simple**
   - Focus on one concept
   - Avoid unnecessary complexity
   - Use realistic examples

4. **Test thoroughly**
   - Verify it works
   - Test edge cases
   - Check for errors

### Creating Exercises

Good exercises should:

1. **Build on tutorials**
   - Reinforce concepts taught
   - Progressive difficulty
   - Clear instructions

2. **Be achievable**
   - Appropriate for skill level
   - Reasonable scope
   - Provide hints if needed

3. **Include solutions**
   - Complete working code
   - Explanatory comments
   - Alternative approaches

Example exercise template:

```python
"""
Exercise: [Exercise Name]

TASK: [Clear description of what to build]

Instructions:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Expected Output:
[Show what the output should look like]

BONUS: [Optional challenge]
"""

# TODO: Your code here
```

### Adding New Modules

To add a new module:

1. **Create module structure**
   ```bash
   mkdir -p modules/0X_module_name/{examples,exercises,solutions}
   ```

2. **Create README.md**
   - Overview and objectives
   - Prerequisites
   - Topics covered
   - Estimated time

3. **Create tutorial.md**
   - Step-by-step guide
   - Code examples
   - Explanations
   - Practical exercises

4. **Add examples**
   - Multiple working examples
   - Progressive complexity
   - Well-commented code

5. **Update main README**
   - Add to table of contents
   - Update project structure
   - Include in learning path

## Pull Request Process

### Before Submitting

- [ ] Code runs without errors
- [ ] Examples are tested
- [ ] Documentation is updated
- [ ] Follows style guidelines
- [ ] Commits are clear and atomic
- [ ] No sensitive data included

### Submitting PR

1. **Create descriptive PR title**
   - "Add: [feature]"
   - "Fix: [bug]"
   - "Update: [component]"
   - "Docs: [improvement]"

2. **Write clear description**
   ```markdown
   ## What does this PR do?
   [Brief description]
   
   ## Changes made
   - [Change 1]
   - [Change 2]
   
   ## Testing
   [How you tested]
   
   ## Related issues
   Fixes #[issue number]
   ```

3. **Request review**
   - Tag relevant maintainers
   - Be responsive to feedback
   - Make requested changes

### After Submission

- Monitor for feedback
- Respond to comments
- Update based on reviews
- Be patient and respectful

## Code Review Guidelines

### As a Reviewer

- Be constructive and kind
- Explain reasoning
- Suggest improvements
- Acknowledge good work
- Focus on code, not person

### As an Author

- Be open to feedback
- Ask questions if unclear
- Make requested changes
- Thank reviewers
- Learn from comments

## Testing

### Manual Testing

Test your changes:
- Run all affected examples
- Verify exercises work
- Check links and references
- Test on different systems

### Example Testing Checklist

- [ ] Code executes without errors
- [ ] Examples produce expected output
- [ ] Dependencies are documented
- [ ] Works with specified Python versions
- [ ] No hardcoded paths or credentials

## Documentation Standards

### Writing Style

- **Clear and concise**: Avoid jargon
- **Beginner-friendly**: Explain concepts
- **Practical**: Include real examples
- **Accurate**: Verify technical details

### Code Examples

- Include file headers
- Add inline comments
- Show imports
- Handle errors
- Provide context

### Tutorial Format

1. **Introduction**
   - What you'll learn
   - Prerequisites

2. **Concepts**
   - Explanations
   - Visual aids

3. **Examples**
   - Working code
   - Step-by-step

4. **Practice**
   - Exercises
   - Solutions

5. **Summary**
   - Key takeaways
   - Next steps

## Ethical Guidelines

All contributions must:
- Promote ethical scraping
- Respect website terms of service
- Include rate limiting examples
- Emphasize legal compliance
- Protect user privacy

❌ **Don't include:**
- Scrapers for paywalled content
- Bypassing authentication
- Harvesting personal data
- Malicious techniques

## Community Guidelines

### Be Respectful

- Welcome newcomers
- Value diverse perspectives
- Give constructive feedback
- Assume good intentions

### Be Collaborative

- Share knowledge
- Help others learn
- Celebrate contributions
- Build together

### Be Ethical

- Follow best practices
- Promote responsible scraping
- Consider legal implications
- Respect privacy

## Getting Help

### Questions?

- Open a discussion on GitHub
- Check existing issues
- Review documentation
- Ask in pull request comments

### Need Maintainer Help?

Tag maintainers in:
- Complex technical issues
- Design decisions
- Merge conflicts
- Policy questions

## Recognition

Contributors will be:
- Listed in README acknowledgments
- Credited in relevant modules
- Thanked in release notes
- Part of the community

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

---

**Thank you for contributing to web scraping education!** 🙏

Every contribution, no matter how small, helps students learn and grow.
