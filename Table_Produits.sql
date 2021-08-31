DROP TABLE IF EXISTS `produits`;
CREATE TABLE `produits` (
  `pharmacieIdBJC` int DEFAULT NULL,
  `upc` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
  `sap` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `idItem` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `fournisseur` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `coutant` double DEFAULT NULL,
  `prix` double DEFAULT NULL,
  `categorie` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sousDepartement` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `departement` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `marque` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `din` varchar(8) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `crx` varchar(6) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `estTaxableFed` tinyint(1) DEFAULT NULL,
  `estTaxableProv` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idItem`,`upc`),
  KEY `IX_upc` (`upc`),
  KEY `IX_sap` (`sap`),
  KEY `IX_DIN` (`din`),
  KEY `IX_DEP` (`departement`),
  KEY `IX_SOUSDEP` (`sousDepartement`),
  KEY `IX_CAT` (`categorie`),
  FULLTEXT KEY `IX_DESC` (`description`),
  FULLTEXT KEY `IX_upc_fulltext` (`upc`)
);

