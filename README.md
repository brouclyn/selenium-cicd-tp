1. Avantages observés

Avantages de l’automatisation des tests
L’automatisation des tests permet de vérifier rapidement que l’application fonctionne toujours après une modification du code. On gagne du temps par rapport aux tests manuels et on évite d’oublier des cas de test. Les mêmes tests peuvent être relancés autant de fois que nécessaire sans effort supplémentaire.

Apport du CI/CD sur la qualité du code
Le CI/CD permet de tester automatiquement le code à chaque push ou pull request. Ça évite d’intégrer du code qui ne fonctionne pas et ça force à corriger les erreurs avant de passer sur la branche principale. Au final, le code est plus propre et plus stable.

2. Défis rencontrés

Difficultés avec Selenium
Avec Selenium, les principales difficultés viennent du chargement des pages et des éléments qui ne sont pas toujours disponibles immédiatement. Certains tests peuvent échouer si on n’attend pas correctement les éléments. Il y a aussi des différences de comportement selon le navigateur ou l’environnement.

Amélioration de la stabilité des tests
Pour améliorer la stabilité, il faut utiliser des attentes explicites plutôt que des pauses fixes. Le Page Object Pattern aide aussi à mieux organiser les tests et à éviter la duplication de code. Tester sur plusieurs navigateurs permet de repérer plus tôt les problèmes.

3. Métriques

Métriques importantes pour le projet
Les métriques les plus importantes sont le nombre de tests qui passent ou échouent, le temps d’exécution des tests et la couverture de code. Elles donnent une bonne idée de la fiabilité du projet.

Mesure de l’efficacité du pipeline CI/CD
L’efficacité du pipeline se mesure par le fait que les erreurs sont détectées rapidement après un changement de code. Un bon pipeline est stable, s’exécute sans problème et permet de corriger rapidement quand quelque chose casse.