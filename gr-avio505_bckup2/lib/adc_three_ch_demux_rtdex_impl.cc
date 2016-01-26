/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <iostream>
#include <gnuradio/io_signature.h>

#include <gnuradio/io_signature.h>
#include "adc_three_ch_demux_rtdex_impl.h"


 #include <volk/volk.h>

#include <functional>   // std::bit_xor
 

 

using namespace std;

namespace gr {
  namespace avio505 {

    adc_three_ch_demux_rtdex::sptr
    adc_three_ch_demux_rtdex::make()
    {
      return gnuradio::get_initial_sptr
        (new adc_three_ch_demux_rtdex_impl());
    }

    /*
     * The private constructor
     */
    adc_three_ch_demux_rtdex_impl::adc_three_ch_demux_rtdex_impl()
      : gr::block("adc_three_ch_demux_rtdex",
              gr::io_signature::make(1, 1, sizeof(short)),
              gr::io_signature::make3(3, 3, sizeof(gr_complex), sizeof(gr_complex), sizeof(gr_complex))
              )
    {
      check_flag_bit = 0;
      flag_start = 32768;
      nit =0;
      n_previous = 0;
      counter2 =0;
      counter_in =0;
	  set_history(200);
	  set_output_multiple(6);	

      const int alignment_multiple = 
              volk_get_alignment() / sizeof(short);
      set_alignment(std::max(1, alignment_multiple));
      counter = 0;
      in_to_floats = (float*)volk_malloc(sizeof(float)*8192 ,  alignment_multiple   );
      in_to_complex = (gr_complex*)in_to_floats;
      in_wo_header = (short*)volk_malloc(sizeof(short)*16383,  alignment_multiple   );
    }

    /*
     * Our virtual destructor.
     */
    adc_three_ch_demux_rtdex_impl::~adc_three_ch_demux_rtdex_impl()
    {
    }

    void
    adc_three_ch_demux_rtdex_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        /* <+forecast+> e.g. */
      //ninput_items_required[0] =  noutput_items;
       ninput_items_required[0] =  8192*2; 
    }

    

    int
    adc_three_ch_demux_rtdex_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const short *in = (short*) input_items[0];
        gr_complex *out_dme1 = (gr_complex*) output_items[0];
        gr_complex *out_dme2 = (gr_complex*) output_items[1];
        gr_complex *out_adsb = (gr_complex*) output_items[2];

        unsigned int escala = 32767;
 
        //int nin_to_process = int( floor(noutput_items/12.0) )*12;
        
        int nin_to_process = int( floor(ninput_items[0]/12.0) )*12;
        int nout_generated = nin_to_process/12;

        unsigned short resu;
        counter= counter + nout_generated;
        counter_in +=  nin_to_process;
        counter2++;
        

          unsigned int n = 0;

          for(int k = 0; k<12; k++){
            resu = (in[k]&flag_start); 
            
            
            if( resu != 0){
               n=k;
            }    
          }
          
          if (n != n_previous){
			 cout <<  "n value has changed "<< n <<  " " << n_previous<<endl; 
			//cout << "sequence number = " << dec<< counter2 << endl;	
			  //cout << "\t******************************************" << endl;
              //cout << "\tin, resu  " << hex << in[n] <<   " \t"  <<    resu   <<     endl;
              //cout << "\tnoutput_items= " << dec << noutput_items <<" \tnin_to_process" << nin_to_process<< endl;
              //cout << "\tninput_items= " << dec << ninput_items[0] <<endl;
              //cout << "\tcounters= " << dec << counter*1.0 <<endl;
              //cout << "\tcounter_in= " << dec << counter_in*1.0 << "  /12= "<<  
                  //setprecision(8) << counter_in/12.0 
                      //<< " nitems_written= " <<  nitems_written(0)<<  endl;
                      
             //cout   <<" \tlast_nin_to_process = " << last_nin_to_process<< endl;       
             //cout   <<" \tlast_nout_generated = " << last_nout_generated << " x12=" << last_nout_generated*12 << endl;         
             //cout   <<" \tlast_ninput_items = " <<  last_ninput_items << endl;       
                      
                      
              cout << "******************************************" << endl;
              
			
		  }
		  n_previous = n;
		   
		   
		  //if( counter2%3000 == 0){
			  //cout << "******************************************" << endl;
              //cout << "in, resu  " << hex << in[n] <<   " \t"  <<    resu   <<     endl;
              //cout << "noutput_items= " << dec << noutput_items <<" \tnin_to_process" << nin_to_process<< endl;
              //cout << "ninput_items= " << dec << ninput_items[0] <<endl;
              //cout << "counters= " << dec << counter*1.0 <<endl;
              //cout << "counter_in= " << dec << counter_in*1.0 << "  /12= "<<counter_in/12.0   <<endl;
              
             //cout   <<" \tlast_nin_to_process = " << last_nin_to_process<< endl;       
             //cout   <<" \tlast_nout_generated = " << last_nout_generated<< " x12=" << last_nout_generated*12   << endl;         
                      
              //cout << "******************************************" << endl;
              
          //} 
          
          int k;
          for (k = 0; k < nin_to_process; k++){
            in_wo_header[k] =  in[k] << 1;
          }
       // cout << "n =" << n << endl;
        unsigned int N;
        
        nit +=  ninput_items[0];

        // N = (unsigned int*)ninput_items;

        volk_16i_s32f_convert_32f(in_to_floats, in_wo_header, escala, nin_to_process);

        unsigned int indexes_dme1[2];
        unsigned int indexes_dme2[2];
        unsigned int indexes[12];

        unsigned int indexes_adbs[12];

        
        indexes_dme1[0] =  n%12;
        indexes_dme1[1] = (n+1)%12; 
        indexes_dme2[0] = (n+2)%12;
        indexes_dme2[1] = (n+3)%12; 

        indexes_adbs[0] = (n+4)%12;
        indexes_adbs[1] = (n+5)%12; 
        indexes_adbs[2] = (n+6)%12; 
        indexes_adbs[3] = (n+7)%12; 
        indexes_adbs[4] = (n+8)%12;
        indexes_adbs[5] = (n+9)%12; 
        indexes_adbs[6] = (n+10)%12; 
        indexes_adbs[7] = (n+11)%12;

        // std::vector<unsigned int> indexes_adbs;
        // for (int i=1; i<8; ++i) indexes_adbs.push_back(  ((n+4)%12)  ); // 1 2 3 4 5 6 7 8 9
        // std::rotate(indexes_adbs.begin(),indexes_adbs.begin()+n,indexes_adbs.end());
        
        std::vector<unsigned int> mya ;
        for (int i=0; i<8; i++) mya.push_back( indexes_adbs[i]  ); // 1 2 3 4 5 6 7 8 9

        unsigned int pr;
        if (n==10){
          pr = 0;
        }else{
          pr = (16-n)%8;
        }
        
          
        std::rotate(mya.begin(),mya.begin()+pr,mya.end());

        std::vector<unsigned int>::iterator it=mya.begin();

        unsigned int geo[8];

        for (k =0; k<8; k++){
          geo[k]= *it;
          it = it + 1;
          // if (k==7) cout << " "<< *it;
          // cout<< dec <<  geo[k]*1.0 << " //";
        }


        indexes[0] = (n+4)%12;
        indexes[1] = (n+5)%12; 
        indexes[2] = (n+6)%12; 
        indexes[3] = (n+7)%12; 
        indexes[4] = (n+4)%12;
        indexes[5] = (n+5)%12; 
        indexes[6] = (n+6)%12; 
        indexes[7] = (n+7)%12; 
        indexes[8] = (n+8)%12; 
        indexes[9] = (n+9)%12; 
        indexes[10] =(n+10)%12; 
        indexes[11] =(n+11)%12; 



        for( int i = 0; i < nout_generated; i++ ){
          // if (i == 900000){
          //   out_dme1[i]   =    gr_complex( 1 , 1 );
          //   out_dme2[i]   =    gr_complex( 1,  1 );
          //   out_adsb[i*4 +0]=  gr_complex( 1 , 1 );
          //   out_adsb[i*4 +1]=  gr_complex( 1 , 1 );
          //   out_adsb[i*4 +2]=  gr_complex( 1 , 1 );
          //   out_adsb[i*4 +3]=  gr_complex( 1 , 1 );
          // }else{
            out_dme1[i]   =    gr_complex( in_to_floats[ i*12 + indexes_dme1[0] ] , in_to_floats[ i*12 + indexes_dme1[1] ] );
            out_dme2[i]   =    gr_complex( in_to_floats[ i*12 + indexes_dme2[0] ] , in_to_floats[ i*12 + indexes_dme2[1] ] );
            out_adsb[i*4 +0]=  gr_complex( in_to_floats[ i*12 + geo[0] ] , in_to_floats[ i*12 + geo[1] ] );
            out_adsb[i*4 +1]=  gr_complex( in_to_floats[ i*12 + geo[2] ] , in_to_floats[ i*12 + geo[3] ] );
            out_adsb[i*4 +2]=  gr_complex( in_to_floats[ i*12 + geo[4] ] , in_to_floats[ i*12 + geo[5] ] );
            out_adsb[i*4 +3]=  gr_complex( in_to_floats[ i*12 + geo[6] ] , in_to_floats[ i*12 + geo[7] ] );
          // }
        }


		/*
       if( counter%3000 == 0){
			for (int mm = 0; mm <12; mm++){  
			  resu = (in[mm]&flag_start); 
			  cout << "indexes["<<mm<< "] =" << indexes[mm] << " " <<hex << in[mm] <<   " \t"  <<    resu<<     endl   <<     endl;

			} 
			cout << endl;
			cout << "n =" << n << endl;
			cout <<  "flag_start "   << hex <<flag_start   << endl;  
			cout << "" << endl;
			cout<< "\nTotal nout_generated = " << counter*1.0 << "\ttime = "<< (counter/1000000.0)<<endl<<endl;
	 
		   

		  cout << "\nindexes_adbs[0:7] = \t\t" ;
		   for (k  =0;  k < 8; k++) cout << indexes_adbs[k] << "   ";
		  cout << "\nrot. indexes_adbs[0:7] = \t" ;
		   for (k  =0;  k < 8; k++) cout << geo[k] << "   ";



		   cout <<endl;
			cout<< " noutput_items= " << noutput_items   <<  "\t" << noutput_items*1.00 <<endl;
			cout<< " ninput_items = " << ninput_items[0]*1.0 << "\ttime = "<< setprecision(3) << nit*1.0*3.0/1000000.0  <<endl;
			  if(  nout_generated +101 > 100){ 
				int k;
				for (k  =0;  k < 12*2; k++){
					cout << "k =\t"<< k*1.0         << "  k %12 =\t"<< (k%12)*1.0       << "\t"<<  std::hex;
					cout <<      in[k]   << '\t'<<dec << nout_generated*1.0 <<    "  " <<nin_to_process <<  endl;

				}
			  }
        }*/

        // Do <+signal processing+>
        // Tell runtime system how many input items we consumed on
        // each input stream.
        last_nin_to_process = nin_to_process;
        last_nout_generated = nout_generated;
        
        last_ninput_items   =  ninput_items[0];
         
        
        consume_each (nin_to_process);

        // Tell runtime system how many output items we produced.


        produce(0, nout_generated);
        produce(1, nout_generated);
        produce(2, nout_generated*4);
        return  0 ;
        

    }

  } /* namespace avio505 */
} /* namespace gr */

