-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema MyNextPromoApp
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `MyNextPromoApp` ;

-- -----------------------------------------------------
-- Schema MyNextPromoApp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `MyNextPromoApp` DEFAULT CHARACTER SET utf8 ;
USE `MyNextPromoApp` ;

-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`admin_users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`admin_users` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`admin_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`accounts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`accounts` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`accounts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `account_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `admin_users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `admin_users_id`),
  INDEX `fk_accounts_admin_users1_idx` (`admin_users_id` ASC) VISIBLE,
  CONSTRAINT `fk_accounts_admin_users1`
    FOREIGN KEY (`admin_users_id`)
    REFERENCES `MyNextPromoApp`.`admin_users` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`certifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`certifications` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`certifications` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `value` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`positions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`positions` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`positions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`other qualifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`other qualifications` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`other qualifications` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `education` VARCHAR(255) NULL,
  `certification` VARCHAR(255) NULL,
  `start_date` DATETIME NULL,
  `end_date` DATETIME NULL,
  `value` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`collateral_duties`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`collateral_duties` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`collateral_duties` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `value` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`positions_has_certifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`positions_has_certifications` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`positions_has_certifications` (
  `position_id` INT NOT NULL,
  `certification_id` INT NOT NULL,
  PRIMARY KEY (`position_id`, `certification_id`),
  INDEX `fk_positions_has_certifications_certifications1_idx` (`certification_id` ASC) VISIBLE,
  INDEX `fk_positions_has_certifications_positions1_idx` (`position_id` ASC) VISIBLE,
  CONSTRAINT `fk_positions_has_certifications_positions1`
    FOREIGN KEY (`position_id`)
    REFERENCES `MyNextPromoApp`.`positions` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_positions_has_certifications_certifications1`
    FOREIGN KEY (`certification_id`)
    REFERENCES `MyNextPromoApp`.`certifications` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`open_positions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`open_positions` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`open_positions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`Employees`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`Employees` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`Employees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `position` VARCHAR(255) NULL,
  `gs_level` VARCHAR(255) NULL,
  `veteran` TINYINT NULL,
  `years_of_service` INT NULL,
  `potential_hire` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `account_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Employees_users1_idx` (`account_id` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_users1`
    FOREIGN KEY (`account_id`)
    REFERENCES `MyNextPromoApp`.`accounts` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`Employees_has_certifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`Employees_has_certifications` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`Employees_has_certifications` (
  `Employee_id` INT NOT NULL,
  `certification_id` INT NOT NULL,
  PRIMARY KEY (`Employee_id`, `certification_id`),
  INDEX `fk_Employees_has_certifications_certifications1_idx` (`certification_id` ASC) VISIBLE,
  INDEX `fk_Employees_has_certifications_Employees1_idx` (`Employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_has_certifications_Employees1`
    FOREIGN KEY (`Employee_id`)
    REFERENCES `MyNextPromoApp`.`Employees` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employees_has_certifications_certifications1`
    FOREIGN KEY (`certification_id`)
    REFERENCES `MyNextPromoApp`.`certifications` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`Employees_has_open_positions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`Employees_has_open_positions` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`Employees_has_open_positions` (
  `Employee_id` INT NOT NULL,
  `open_position_id` INT NOT NULL,
  PRIMARY KEY (`Employee_id`, `open_position_id`),
  INDEX `fk_Employees_has_open_positions_open_positions1_idx` (`open_position_id` ASC) VISIBLE,
  INDEX `fk_Employees_has_open_positions_Employees1_idx` (`Employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_has_open_positions_Employees1`
    FOREIGN KEY (`Employee_id`)
    REFERENCES `MyNextPromoApp`.`Employees` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employees_has_open_positions_open_positions1`
    FOREIGN KEY (`open_position_id`)
    REFERENCES `MyNextPromoApp`.`open_positions` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`Employees_has_other qualifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`Employees_has_other qualifications` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`Employees_has_other qualifications` (
  `Employee_id` INT NOT NULL,
  `other qualification_id` INT NOT NULL,
  PRIMARY KEY (`Employee_id`, `other qualification_id`),
  INDEX `fk_Employees_has_other qualifications_other qualifications1_idx` (`other qualification_id` ASC) VISIBLE,
  INDEX `fk_Employees_has_other qualifications_Employees1_idx` (`Employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_has_other qualifications_Employees1`
    FOREIGN KEY (`Employee_id`)
    REFERENCES `MyNextPromoApp`.`Employees` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employees_has_other qualifications_other qualifications1`
    FOREIGN KEY (`other qualification_id`)
    REFERENCES `MyNextPromoApp`.`other qualifications` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`Employees_has_collateral_duties`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`Employees_has_collateral_duties` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`Employees_has_collateral_duties` (
  `Employee_id` INT NOT NULL,
  `collateral_duty_id` INT NOT NULL,
  PRIMARY KEY (`Employee_id`, `collateral_duty_id`),
  INDEX `fk_Employees_has_collateral_duties_collateral_duties1_idx` (`collateral_duty_id` ASC) VISIBLE,
  INDEX `fk_Employees_has_collateral_duties_Employees1_idx` (`Employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_has_collateral_duties_Employees1`
    FOREIGN KEY (`Employee_id`)
    REFERENCES `MyNextPromoApp`.`Employees` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employees_has_collateral_duties_collateral_duties1`
    FOREIGN KEY (`collateral_duty_id`)
    REFERENCES `MyNextPromoApp`.`collateral_duties` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MyNextPromoApp`.`Employees_has_positions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `MyNextPromoApp`.`Employees_has_positions` ;

CREATE TABLE IF NOT EXISTS `MyNextPromoApp`.`Employees_has_positions` (
  `Employee_id` INT NOT NULL,
  `position_id` INT NOT NULL,
  PRIMARY KEY (`Employee_id`, `position_id`),
  INDEX `fk_Employees_has_positions_positions1_idx` (`position_id` ASC) VISIBLE,
  INDEX `fk_Employees_has_positions_Employees1_idx` (`Employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_has_positions_Employees1`
    FOREIGN KEY (`Employee_id`)
    REFERENCES `MyNextPromoApp`.`Employees` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employees_has_positions_positions1`
    FOREIGN KEY (`position_id`)
    REFERENCES `MyNextPromoApp`.`positions` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
