import pytest
import project
from unittest.mock import patch, mock_open

def test_get_page_content_success():
    """Test la récupération réussie d'une page"""
    with patch('requests.get') as mock_get:
        # Configuration du mock
        mock_response = mock_get.return_value
        mock_response.text = "<html>Test content</html>"
        mock_response.raise_for_status.return_value = None

        url = "https://books.toscrape.com/catalogue/page-1.html"
        content = project.get_page_content(url)

        # Vérifications
        assert content == "<html>Test content</html>"
        mock_get.assert_called_once_with(url)

def test_get_page_content_failure():
    """Test l'échec de récupération d'une page"""
    with patch('requests.get') as mock_get:
        # Simulation d'une erreur de requête
        mock_get.side_effect = project.requests.exceptions.RequestException()

        url = "https://site-invalide.com"
        content = project.get_page_content(url)

        # Vérifications
        assert content is None
        mock_get.assert_called_once_with(url)

def test_extract_titles():
    """Test l'extraction des titres depuis le HTML"""
    test_html = """
    <html>
        <section>
            <h3><a title="Le Petit Prince"></a></h3>
            <h3><a title="1984"></a></h3>
            <h3><a title="Notre-Dame de Paris"></a></h3>
        </section>
    </html>
    """

    titles = project.extract_titles(test_html)

    # Vérifications
    assert len(titles) == 3
    assert titles == ["Le Petit Prince", "1984", "Notre-Dame de Paris"]

def test_extract_titles_empty():
    """Test l'extraction des titres avec une section vide"""
    test_html = """
    <html>
        <section>
        </section>
    </html>
    """

    titles = project.extract_titles(test_html)
    assert len(titles) == 0

def test_scrape_books(tmp_path):
    """Test le scraping complet des livres"""
    with patch('project.get_page_content') as mock_get_content:
        with patch('project.extract_titles') as mock_extract:
            # Simulation de 2 pages de résultats
            mock_get_content.side_effect = [
                "page1 content",
                "page2 content",
                None
            ]
            mock_extract.side_effect = [
                ["Titre 1", "Titre 2"],
                ["Titre 3", "Titre 4"]
            ]

            # Création d'un fichier temporaire pour les tests
            test_file = tmp_path / "titles.txt"

            # Test de l'écriture dans le fichier
            with patch('builtins.open', create=True) as mock_file:
                project.scrape_books()

                # Vérifications
                assert mock_get_content.call_count == 3
                assert mock_extract.call_count == 2
                mock_file.assert_called_once()

def test_main():
    """Test la fonction principale"""
    with patch('project.scrape_books') as mock_scrape:
        project.main()
        mock_scrape.assert_called_once()

def test_extract_titles_invalid_html():
    """Test l'extraction des titres avec un HTML invalide"""
    with pytest.raises(AttributeError):
        project.extract_titles("Invalid HTML")

def test_get_page_content_http_error():
    """Test la gestion des erreurs HTTP"""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = project.requests.exceptions.HTTPError()

        url = "https://books.toscrape.com/catalogue/page-999.html"
        content = project.get_page_content(url)

        assert content is None
