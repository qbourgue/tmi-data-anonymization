require 'data-anonymization'
require 'mongo'

DataAnon::Utils::Logging.logger.level = Logger::INFO

connection_spec = {:host => '127.0.0.1', :port => '27017', :database => 'naisdb'}

database 'test' do

  strategy DataAnon::Strategy::MongoDB::Whitelist
  source_db :mongodb_uri => 'mongodb://127.0.0.1:27017/naisdb', :database => 'naisdb'
  destination_db :mongodb_uri => 'mongodb://127.0.0.1:27017/anony_naisdb', :database => 'anony_naisdb'

	collection 'very_short_table' do
		whitelist '_id'
		whitelist 'ID'
		whitelist 'SEXE'
		whitelist 'ANAIS'
		anonymize('MNAIS').using FieldStrategy::RandomInteger.new(1,12)
		anonymize('DEPNAIS').using FieldStrategy::RandomInteger.new(1,95)
		anonymize('JRECP').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('MRECP').using FieldStrategy::RandomInteger.new(1,12)
		whitelist 'ARECP'
		anonymize('JRECM').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('MRECM').using FieldStrategy::RandomInteger.new(1,12)
		whitelist 'ARECM'
		anonymize('JRECC').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('MRECC').using FieldStrategy::RandomInteger.new(1,12)
		whitelist 'ARECC'
		anonymize('AGEMERE').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('AGEXACTM').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('INDLNM').using FieldStrategy::SelectFromDatabase.new('very_short_table','INDLNM', connection_spec)
		anonymize('SITUATMR').using FieldStrategy::SelectFromDatabase.new('very_short_table','SITUATMR', connection_spec)
		anonymize('INDNATM').using FieldStrategy::SelectFromDatabase.new('very_short_table','INDNATM', connection_spec)
		anonymize('DEPDOM').using FieldStrategy::RandomInteger.new(1,95)
		anonymize('TUDOM').using FieldStrategy::SelectFromDatabase.new('very_short_table','TUDOM', connection_spec)
		anonymize('TUCOM').using FieldStrategy::SelectFromDatabase.new('very_short_table','TUCOM', connection_spec)
		anonymize('AGEPERE').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('AGEXACTP').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('INDLNP').using FieldStrategy::SelectFromDatabase.new('very_short_table','INDLNP', connection_spec)
		anonymize('SITUATPR').using FieldStrategy::SelectFromDatabase.new('very_short_table','SITUATPR', connection_spec)
		anonymize('INDNATP').using FieldStrategy::SelectFromDatabase.new('very_short_table','INDNATP', connection_spec)
		anonymize('AMAR').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('DMARNAIS').using FieldStrategy::SelectFromDatabase.new('very_short_table','DMARNAIS', connection_spec)
		anonymize('ACCOUCHR').using FieldStrategy::SelectFromDatabase.new('very_short_table','ACCOUCHR', connection_spec)
		anonymize('NBENF').using FieldStrategy::SelectFromDatabase.new('very_short_table','NBENF', connection_spec)
		anonymize('DURECEVP').using FieldStrategy::RandomIntegerDelta.new(3)
		anonymize('ORIGINOM').using FieldStrategy::SelectFromDatabase.new('very_short_table','ORIGINOM', connection_spec)
	end


end

